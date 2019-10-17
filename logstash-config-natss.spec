Name:		logstash-config-natss
Version:	0.1
Release:	1%{?dist}
Summary:	Logstash config files for the NATSS Logstash Servers

Group:		Engineering
BuildArch:	noarch
License:	NATSS
#URL:		
#Source0:	logstash-config-natss.tar.gz

#BuildRequires:	
Requires:	bash

%description
Version 1.0 of logstash configs.


%prep
#%setup -q

# Not using setup macro here, type out the commands to copy the files manually
cd %{_topdir}/BUILD
rm -rf %{name}-%{version}
cp -rf %{_topdir}/SOURCES/%{name}/* .
cd %{name}
chmod -Rf a+rx,u+w,g-w,o-w .

%build
cd %{name}

%install
mkdir -p %{buildroot}/etc/logstash
cp -r ./* %{buildroot}/etc/logstash

%files
# Default Attributes for the package
%defattr(644, root, root, 755)
/*

# Set the private key attributes to be more strict
%attr(600, logstash, root) /etc/logstash/keys/*.key

%doc

%changelog
* Wed Oct 16 2019 Alfonso Brown 0.1-1
  - Initial creation of RPM (testing)
