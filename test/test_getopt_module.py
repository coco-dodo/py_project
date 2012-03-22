#!/usr/bin/python
import getopt, sys
def usage():
	pass

def main():
    try:
    	opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
	except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
	    usage()
        sys.exit(2)	

    output = None
    verbose = False
    
	for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
			print output
        else:
            assert False, "unhandled option"
    # ...

if __name__ == "__main__":
    main()

