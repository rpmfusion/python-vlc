# [Fedora] Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%global gitdate 20161001git5d389c7

Name:           python-vlc
Version:        1.1.2
Release:        1.%{gitdate}%{?dist}
Summary:        VLC Media Player binding for Python
Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://www.videolan.org/
Source0:        %{name}-%{version}-%{gitdate}.tar.bz2
Source9:        %{name}-snapshot.sh
BuildArch:      noarch
BuildRequires:  python2-devel
Requires:       vlc-core >= 1.1.0

%description
This package provides a python interface to control VLC Media Player.

%prep
%setup -q

%build
# The vlc.py file is already generated
%py2_build

%install
%py2_install

mkdir -p %{buildroot}%{_datadir}/%{name}/examples
install -pm 755 examples/* \
   %{buildroot}%{_datadir}/%{name}/examples/

#fix rpmlint
chmod +x %{buildroot}%{python2_sitelib}/*py

%check
%{__python2} setup.py test


%files
%doc README.rst TODO
%{python2_sitelib}/vlc.py*
%{python2_sitelib}/*egg-info
%{_datadir}/%{name}/


%changelog
* Sat Oct 01 2016 Sérgio Basto <sergio@serjux.com> - 1.1.2-1.20161001git5d389c7
- Add git tag to version.
- Update to 1.1.2-20161001git5d389c7
- Update python snippets.

* Mon Aug 01 2016 Sérgio Basto <sergio@serjux.com> - 1.1.0-9.20141115git
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Nov 15 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-8.20120503git
- Update to today's snapshot

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.1.0-7.20120503git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-6.20120503git
- Mass rebuilt for Fedora 19 Features

* Thu May 03 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-5.20120503git
- Update to current snapshot

* Sun Dec 25 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.1.0-4.20111225git
- Latest git snapshot.

* Sat Dec 17 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-3.20100825git
- Rebuild for vlc-1.2.x

* Wed Aug 25 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.1.0-2.20100825git
- Latest git snapshot.
- Build against python-2.7 on F-14

* Tue Jul 06 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.1.0-1.20100706git
- 1.1.0 final updates

* Tue May 11 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.1.0-0.1.20100511git
- Update to 1.1.0 (git checkout)

* Fri Jun 19 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.0.0-0.2.90
- Remove COPYING file

* Sat May 30 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.0.0-0.1.90
- New checkout from 1.0-bugfix
- Some specfile clean-up

* Sun Feb 08 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.8a-1.20090218git
- Package python-vlc separately since vlc doesn't provide it in its tarball anymore.
