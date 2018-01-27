#!/usr/bin/python
"""
    Main program entry

    Author: kevinbird61
"""

import argparse

parser = argparse.ArgumentParser(description='Meme Face Generator')
parser.add_argument('--img',help='Specify the image url of your face',
                    type=str,action="store",required=True)
parser.add_argument('--model',help='Specify the background template you want',
                    type=str,action="store",default="panda_man")
parser.add_argument('--model_url',help='Specify the background template from user',
                    type=str,action="store",default=None)

args = parser.parse_args()

def main():
    print "Welcome to use meme_face generator!"
    print 

    img_url=args.img
    model=args.model
    model_url=args.model_url

    if model_url != None:
        print "Specified user-defined template: '%s', use it instead of '%s'" % (model_url,model)
        model=model_url
        print "Your image path: '%s', and template you use is '%s'" % (img_url,model)
    else:
        print "Your image path: '%s', and template you use is '%s'" % (img_url,model)
    

if __name__ == '__main__':
    main()