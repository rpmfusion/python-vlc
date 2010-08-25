%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

%global gitdate 20100825git

Name:           python-vlc
Version:        1.1.0
Release:        2.%{gitdate}%{?dist}
Summary:        VLC Media Player binding for Python
Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://www.videolan.org/
Source0:        %{name}-%{version}-%{gitdate}.tar.bz2
Source9:        %{name}-snapshot.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python2-devel
Requires:       vlc-core >= 1.1.0

%description
This package provides a python interface to control VLC Media Player.

%prep
%setup -q

%build
# The vlc.py file is already generated

%install
rm -rf $RPM_BUILD_ROOT
sleep 1m
mkdir -p $RPM_BUILD_ROOT%{python_sitelib}
install -pm 755 generated/vlc.py vlcwidget.py \
   $RPM_BUILD_ROOT%{python_sitelib}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README TODO
%{python_sitelib}/vlc.py*
%{python_sitelib}/vlcwidget.py*

%changelog
* Wed Aug 15 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.1.0-2.20100825git
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
