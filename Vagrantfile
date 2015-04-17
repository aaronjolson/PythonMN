# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.provider :virtualbox do |virtualbox|
    virtualbox.customize ["modifyvm", :id, "--memory", "768"]
    virtualbox.customize ["modifyvm", :id, "--cpus", "4"]
  end

  config.vm.box = "ubuntu/trusty64"

  config.landrush.enabled = true
  config.vm.network 'private_network', type: :dhcp
  config.vm.hostname = "pythonMN.vagrant.dev"

  config.cache.scope = :box
  config.cache.enable :generic, {
    "pip" => { cache_dir: "/var/cache/pip" },
    "wget" => { cache_dir: "/var/cache/wget" },
  }

  config.vm.provision :shell, :path => "Vagrantprovision.sh"

end