#!/usr/bin/env python
import sys
import subprocess
import argparse

command = {}
command["Container"] = {}
command["Image"] = {}
command["Container"]["list"] = "ps"
command["Container"]["remove"] = "rm"
command["Image"]["list"] = "images"
command["Image"]["remove"] = "rmi"

def get_options():
  parser =  argparse.ArgumentParser(description= 'Use this simple command to remove Docker container(s) or images(s) through string matching.')
  parser.add_argument('--container','-c',help="Flag to remove Docker container(s) only")
  parser.add_argument('--image','-i',help="Flag to remove Docker image(s) only")
  parser.add_argument('--name','-n',help="Flag to remove both Docker container(s) and image(s)")
  parser.add_argument('-a',action='store_true',help="Flag to remove hidden container(s)/image(s)")
  parser.add_argument('-f',action='store_true',help="Flag to forcefully remove container(s)/image(s)")
  return parser.parse_args()

def run_cmd(statement):
  process = subprocess.Popen(statement,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  return process.communicate()

def docker_running():
  try:
    out,err = run_cmd(["docker","ps"])
    if err:
      print "Couldn't run Docker due to the following error(s)\n" + err
      sys.exit()
  except:
    print "Docker is not running. Make sure Docker is installed and running"
    sys.exit()

def remove(remove_type,remove_string,hidden,force):
  docker_running()
  print "Removing " + remove_type + "(s) containing string " + remove_string

  list_command = ["docker",command[remove_type]["list"]]
  if hidden == True:
    list_command.append("-a")
  remove_type_list,_ = run_cmd(list_command)
  
  delete_count = 0
  for row in remove_type_list.split("\n"):
    if row.find(remove_string) != -1:
      code = name = None
      if remove_type == "Container":
        code = row.split()[0]
        name = row.split()[1]
      elif remove_type == "Image":
        code = row.split()[2]
        name = row.split()[0]
      
      remove_command = ["docker",command[remove_type]["remove"]]
      if force == True:
        remove_command.append("-f")
      remove_command.append(code)

      out,err = run_cmd(remove_command)

      if not err.split():
        print "Successfully removed " + remove_type + " " + name + " with id " + code
        delete_count = delete_count + 1
      else:
        print "Unable to remove " + remove_type + " " + name + " with id " + code + " due to error : "
        print err
  
  print remove_type + "(s) deleted",delete_count

def main():
  options = get_options()
  if options.container != None:
    remove("Container",options.container,options.a,options.f)
  if options.image != None:
    remove("Image",options.image,options.a,options.f)
  if options.name != None:
    remove("Container",options.name,options.a,options.f)
    remove("Image",options.name,options.a,options.f)

if __name__ == '__main__':
  main()
