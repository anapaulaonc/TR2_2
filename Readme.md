# Description

Projeto 2 de Disciplina TeleInformática e Redes.
Utilizar simulador para SDN com suporte para Openflow - Mininet e criar topologia habilitada para openflow no mininet e fornecer aplicativo que incrementa a segurança em uma rede.
Requisitos mínimos topologia:

- Conter pelo menos um controlador
- 4 switches habilidades para fluxo aberto
- 10 hosts

### aluno

- Ana Paula Nóbrega - 190142120
- Gabriel Cruz Vaz Santos - 200049038
- Nicolas Paulin Benatto - 200025627

# Install Dependencies

To run this project you will need

- pip & pyhton3

```
$ sudo apt install -y python3-pip
$ python3 -V
```

- mininet

```
$ sudo apt-get install mininet
$ sudo apt-get install openvswitch-switch
$ sudo service openvswitch-switch start
```

- openflow

```
$git clone https://github.com/mininet/mininet
$ mininet/util/install.sh -fw
```

# Before Project Run

# Run Project

# References

- [walkthrough mininet](http://mininet.org/walkthrough/)
- [drive document](https://docs.google.com/document/d/1f0QPhMonsCHjrotPNxG3TVrlpLRyDazT0nE1HL6KgOM/edit)
- [install python](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-22-04-server)

# Extra

### config your vscode for fix eslint warnings on auto-save

- Go to File -> preferences -> settings
- On your right-hand side, there is an icon to Open Settings in JSON format. Click on that icon.
- add the following json code inside the settings.json:

  `"editor.codeActionsOnSave": { "source.fixAll.eslint": true }, "editor.formatOnSave": true, "eslint.alwaysShowStatus": true, "files.autoSave": "onFocusChange"`
