set_proxy()
{
  export http_proxy=socks5h://127.0.0.1:1089

  export {https,ftp,rsync,all}_proxy=$http_proxy
  export {HTTP,HTTPS,FTP,RSYNC,ALL}_PROXY=$http_proxy

  export ssh_proxy='ProxyCommand=nc -X 5 -x 127.0.0.1:1089 %h %p'

  no_proxy="127.0.0.1,localhost,.localdomain.com"
  export no_proxy
}

unset_proxy()
{
  unset {http,https,ftp,rsync,all}_proxy {HTTP,HTTPS,FTP,RSYNC,ALL}_PROXY
}

check_proxy()
{
  curl --head www.google.com
}
