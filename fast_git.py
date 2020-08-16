import sys, subprocess, os
mirror = "github.com.cnpmjs.org"
try:
    action = sys.argv[1]
    if action == "clone" or action == "c":
        url = sys.argv[2]
        url_2 = url.replace("github.com", mirror, 1)
        answer = input('[fast_git]You will clone from %s, press "y" to start\n' % url_2)
        if answer == "y":
            pass
        else:
            print("[fast_git]User canceled!")
            sys.exit()
        repository = url.split("/")[4].replace(".git", "")
        clone = subprocess.Popen("git clone %s" % url_2, shell=True)
        clone.wait()
        print("[fast_git]Replacing repository url...")
        os.chdir("%s/" % repository)
        subprocess.Popen("git remote set-url origin %s" % url)
        print("[fast_git]Success!")
except Exception as e:
    print("[fast_git]Error:\t", repr(e))

