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


%changelog
* Wed Mar 30 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.3.0-1mdv2011.0
+ Revision: 649205
- update to 0.3.0
- update doc

* Mon Nov 01 2010 Funda Wang <fwang@mandriva.org> 0.2.1-4mdv2011.0
+ Revision: 591346
- rebuild for py 2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.2.1-3mdv2010.0
+ Revision: 442316
- rebuild

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 0.2.1-2mdv2009.1
+ Revision: 323360
- rebuild

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.1-1mdv2009.1
+ Revision: 305846
- update to new version 0.2.1

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.2.0-2mdv2009.0
+ Revision: 269033
- rebuild early 2009.0 package (before pixel changes)

* Mon May 05 2008 Funda Wang <fwang@mandriva.org> 0.2.0-1mdv2009.0
+ Revision: 201240
- Import source and spec
- Created package structure for python-mpd.

