# [Fedora] Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%global gitdate 20200311git8e6c723
%global srcname vlc
%global sum VLC Media Player binding for Python
%global desc This package provides a python interface to control VLC Media Player.

Name:           python-%{srcname}
Version:        3.0.8112
Release:        0.2.%{gitdate}%{?dist}
Summary:        %{sum}
License:        GPLv2+
URL:            http://www.videolan.org/
Source0:        %{name}-%{version}-%{gitdate}.tar.bz2
Source9:        %{name}-snapshot.sh
BuildArch:      noarch
BuildRequires:  python3-devel

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{sum}
Requires:       vlc-core >= 1.1.0
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
%setup -q
#fix shebang
sed -i "s|#! /usr/bin/python||" examples/*.py
sed -i "s|! /usr/bin/python|! %{__python3}|" generated/3.0/vlc.py

%build
pushd generated/3.0
%py3_build
popd

%install
pushd generated/3.0
%py3_install
popd

mkdir -p %{buildroot}%{_datadir}/%{name}/examples/video_sync
install -pm 755 examples/*.* \
   %{buildroot}%{_datadir}/%{name}/examples/
install -pm 755 examples/video_sync/*.* \
   %{buildroot}%{_datadir}/%{name}/examples/video_sync/

#fix rpmlint
chmod +x %{buildroot}%{python3_sitelib}/*py
chmod -x %{buildroot}%{_datadir}/%{name}/examples/*py
chmod -x %{buildroot}%{_datadir}/%{name}/examples/video_sync/{*.py,README.md}

%check
pushd generated/3.0
%{__python3} setup.py test
popd

%files -n python3-%{srcname}
%license COPYING
%doc README.rst TODO
%{python3_sitelib}/*
%{_datadir}/%{name}/


%changelog
* Sat May 30 2020 Leigh Scott <leigh123linux@gmail.com> - 3.0.8112-0.2.20200311git8e6c723
- Rebuild for python-3.9

* Wed Mar 11 2020 Leigh Scott <leigh123linux@gmail.com> - 3.0.8112-0.1.20200311git8e6c723
- Update to 3.0.8112
- Drop python2 sub package

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.0.6109-0.5.20190508git949d19e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 24 2019 Leigh Scott <leigh123linux@gmail.com> - 3.0.6109-0.4.20190508git949d19e
- Rebuild for python-3.8

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.0.6109-0.3.20190508git949d19e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 08 2019 Leigh Scott <leigh123linux@gmail.com> - 3.0.6109-0.2.20190508git949d19e
- Remove shebang so python2-vlc doesn't require python3

* Wed May 08 2019 Leigh Scott <leigh123linux@gmail.com> - 3.0.6109-0.1.20190508git949d19e
- Update to 3.0.6109
- Remove Group tag

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.1.2-9.20161001git5d389c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
- Fix shebang on examples

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.1.2-8.20161001git5d389c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-7.20161001git5d389c7
- Rebuilt for Python 3.7

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.1.2-6.20161001git5d389c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.1.2-5.20161001git5d389c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.1.2-4.20161001git5d389c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 03 2016 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.1.2-3.20161001git5d389c7
- Skip Python 3 tests

* Mon Oct 03 2016 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.1.2-2.20161001git5d389c7
- Created separate python2 and 3 subpackages

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
