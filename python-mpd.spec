Name:           python-mpd
Version:        0.5.1
Release:        2
Summary:        Python bindings for MPD
Group:          Development/Python
License:        GPL
URL:            https://www.musicpd.org/~jat/python-mpd/
Source0:        http://pypi.python.org/packages/source/p/python-mpd2/python-mpd2-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:  python-devel
BuildRequires:  python-distribute

%description
An MPD (Music Player Daemon) client library written in pure Python.

%prep
%setup -q -n %{name}2-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__python} setup.py install --root %buildroot

%clean

%files
%doc LICENSE.txt GPL.txt
%{py_puresitedir}/*
