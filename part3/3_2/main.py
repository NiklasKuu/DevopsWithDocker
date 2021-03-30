import subprocess, sys, getopt


def main(argv):
    # set git url
    try:
        opts, args = getopt.getopt(argv,"hr:d:u:p:",["gitrepo=","dockerrepo=","username=","password="])
    except getopt.GetoptError:
        print('main.py -r <git repository url> -d <docker repository url> -u <username> -p <password>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -r <git repository url> -d <docker repository url> -u <username> -p <password>')
            sys.exit()
        elif opt in ("-r", "--gitrepo"):
            git_repositoryUrl = arg
        elif opt in ("-d", "--dockerrepo"):
            docker_repositoryUrl = arg
        elif opt in ("-u", "--username"):
            docker_username = arg
        elif opt in ("-p", "--password"):
            docker_password = arg

    print(git_repositoryUrl, docker_repositoryUrl, docker_username, docker_password)

    git_download_process = subprocess.Popen(['git', 'clone', git_repositoryUrl + '.git'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    git_download_output = git_download_process.communicate()
    print(git_download_output[1].decode("utf-8"))
    git_folder_name = git_download_output[1].decode("utf-8").split('\'')[1]
    print(git_folder_name)

    print('Building docker file in folder "' +  git_folder_name + '"')
    subprocess.run(['docker build . -t ' +docker_repositoryUrl+' -f '+ git_folder_name+'/Dockerfile'], shell=True)
    subprocess.run(['docker login -u ' + docker_username + ' -p ' + docker_password], shell=True)
    subprocess.run(['docker push '+ docker_repositoryUrl], shell=True)


if __name__ == "__main__":
   main(sys.argv[1:])