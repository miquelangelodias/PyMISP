#!/bin/bash
_ip=`ifconfig eth0 | grep inet | cut -d"t" -f2 | cut -d" " -f2`
msfdb init
sed -i s/"127.0.0.1"/${_ip}/ \
/opt/metasploit-framework/embedded/framework/plugins/msgrpc.rb
sed -i 's/55552/55553/' \
/opt/metasploit-framework/embedded/framework/plugins/msgrpc.rb
sed -i 's/"msf"/"test"/' \
/opt/metasploit-framework/embedded/framework/plugins/msgrpc.rb
sed -i 's/::Rex::Text.rand_text_alphanumeric(8)/"test1234"/' \
/opt/metasploit-framework/embedded/framework/plugins/msgrpc.rb
msfdb init
msfconsole -p msgrpc -q