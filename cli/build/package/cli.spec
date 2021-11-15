%{!?_version: %define _version 0.1 }
%{!?_major: %define _major %{_version} }
%{!?_branch: %define _branch %(git rev-parse --abbrev-ref HEAD) }

%define _release %(/bin/date +"%Y%m%d.%H%M")

Name:           cli
Version:        %{_version}
Release:        %{_release}
Source0:        %{name}-%{_major}.tar.gz
BuildRoot:      %{_tmppath}/%{name}
License:        Open
Vendor:         Huvalk
Summary:        CLI - CLI

%description
CLI - set of command line tools for electorator

Packager: %(echo ${USER})
BuildHost: %(echo ${HOSTNAME})
Branch: %{_branch}
Commit: %(git rev-parse HEAD)

%prep
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%setup -q -n %{name}
mkdir -p configs/tmp
go run cli/cmd/main.go completion bash > configs/tmp/bash

%build
go build -o build -ldflags "-linkmode=external ./cli/cmd/main.go

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%{__mkdir} -p %{buildroot}/usr/bin
%{__mkdir} -p %{buildroot}/etc/%{name}

%{__install} -pD -m 755 build/cli %{buildroot}/usr/bin
%{__install} -pD -m 644 configs/config.yaml  %{buildroot}/etc/%{name}/config.yaml

%{__install} -pD -m 644 configs/tmp/bash %{buildroot}/etc/bash_completion.d/%{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
rm -rf configs/tmp

%files
/usr/bin/%{name}
%config(noreplace) /etc/%{name}/config.yaml
/etc/bash_completion.d/%{name}
