#!/usr/bin/env bash
#run one time
sudo apt-get update
sudo apt-get install automake autotools-dev g++ git libcurl4-openssl-dev libfuse-dev libssl-dev libxml2-dev make pkg-config
git clone https://github.com/s3fs-fuse/s3fs-fuse.git
cd s3fs-fuse
./autogen.sh
./configure
make

sudo make install
echo "qwra9xCI3vt9Sp5TW63j:uXHsuEjk1jJnxg0twKppYkUVo7EtzIQ6RuqTdo2y" > $HOME/.cos_creds
chmod 600 $HOME/.cos_creds

sudo mkdir /posturedata
sudo s3fs hw3storage /posturedata -o passwd_file=$HOME/.cos_creds -o sigv2 -o use_path_request_style -o url=http://s3.us.cloud-object-storage.appdomain.cloud
# -o nonempty
