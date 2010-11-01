Name:           python-mpd
Version:        0.2.1
Release:        %mkrel 4
Summary:        Python bindings for MPD
Group:          Development/Python
License:        GPL
URL:            http://www.musicpd.org/~jat/python-mpd/
Source0:        http://pypi.python.org/packages/source/p/%name/%name-%version.tar.bz2
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
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.txt TODO.txt
%{python_sitelib}/*
