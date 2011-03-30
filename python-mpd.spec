Name:           python-mpd
Version:        0.3.0
Release:        %mkrel 1
Summary:        Python bindings for MPD
Group:          Development/Python
License:        GPL
URL:            http://www.musicpd.org/~jat/python-mpd/
Source0:        http://pypi.python.org/packages/source/p/%name/%name-%version.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
%py_requires -d

%description
An MPD (Music Player Daemon) client library written in pure Python.

%prep
%setup -q -n %name-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
%{__python} setup.py install --root %buildroot

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%doc LICENSE.txt GPL.txt README.txt CHANGES.txt 
%{python_sitelib}/*
