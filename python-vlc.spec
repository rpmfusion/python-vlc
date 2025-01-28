%global pypi_name python-vlc
%global pypi_version 3.0.20123
%global srcname vlc
%global sum VLC Media Player binding for Python
%global desc This package provides a python interface to control VLC Media Player.

Name:           python-%{srcname}
Version:        %{pypi_version}
Release:        5%{?dist}
Summary:        %{sum}

License:        LGPLv2+
URL:            https://wiki.videolan.org/PythonBinding
Source0:        %{pypi_name}-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{sum}
Requires:       vlc-core >= 1.1.0
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# fix shebang
%py3_shebang_fix \
 examples/*.py \
 vlc.py
#fix rpmlint
chmod -x examples/cocoavlc.py examples/glsurface.py
# Move README.md
mv examples/video_sync/README.md .

%build
%py3_build

%install
%py3_install

#fix rpmlint
chmod +x %{buildroot}%{python3_sitelib}/vlc.py

%files -n python3-%{srcname}
%doc README.module README.md examples/
%license COPYING
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/vlc.py
%{python3_sitelib}/python_vlc-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.0.20123-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.0.20123-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 13 2024 Leigh Scott <leigh123linux@gmail.com> - 3.0.20123-3
- Rebuilt for Python 3.13

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.0.20123-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 14 2023 Leigh Scott <leigh123linux@gmail.com> - 3.0.20123-1
- Update to 3.0.20123

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.0.18122-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Leigh Scott <leigh123linux@gmail.com> - 3.0.18122-2
- Rebuilt for Python 3.12

* Sat Apr 22 2023 Leigh Scott <leigh123linux@gmail.com> - 3.0.18122-1
- Update to 3.0.18122

* Wed Nov 16 2022 Leigh Scott <leigh123linux@gmail.com> - 3.0.18121-1
- Update to 3.0.18121

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.0.16120-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Sat Jun 25 2022 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.16120-2
- Rebuilt for Python 3.11

* Tue Apr 12 2022 Leigh Scott <leigh123linux@gmail.com> - 3.0.16120-1
- Update to 3.0.16120

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.0.11115-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.0.11115-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Leigh Scott <leigh123linux@gmail.com> - 3.0.11115-4
- Rebuild for python-3.10

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.0.11115-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.0.11115-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Leigh Scott <leigh123linux@gmail.com> - 3.0.11115-1
- Update to 3.0.11115

* Mon Jun 15 2020 Leigh Scott <leigh123linux@gmail.com> - 3.0.10114-1
- Update to 3.0.10114

* Thu Jun 11 2020 Leigh Scott <leigh123linux@gmail.com> - 3.0.9113-1
- Update to 3.0.9113
- Fix License
- Move examples to doc

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
