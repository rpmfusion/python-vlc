%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%global ver_min .90

Name:           python-vlc
Version:        1.0.0
Release:        0.2%{ver_min}%{?dist}
Summary:        VLC Media Player binding for Python
Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://www.videolan.org/
Source0:        %{name}-%{version}%{ver_min}.tar.gz
Source9:        %{name}-snapshot.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  vlc-devel

%description
This package provides a python interface to control VLC Media Player.

%prep
%setup -q -n %{name}-%{version}%{ver_min}

%build
CFLAGS="$RPM_OPT_FLAGS" python -c 'import setuptools; execfile("setup.py")' build

%install
rm -rf $RPM_BUILD_ROOT
python -c 'import setuptools; execfile("setup.py")' install --skip-build --root $RPM_BUILD_ROOT

# Correct the permission of the script
chmod +x $RPM_BUILD_ROOT%{python_sitearch}/vlcwidget.py
 
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{python_sitearch}/*egg-info
%{python_sitearch}/vlc.so
%{python_sitearch}/vlcwidget.py*

%changelog
* Fri Jun 19 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.0.0-0.2.90
- Remove COPYING file

* Sat May 30 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.0.0-0.1.90
- New checkout from 1.0-bugfix
- Some specfile clean-up

* Sun Feb 08 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 0.9.8a-1.20090218git
- Package python-vlc separately since vlc doesn't provide it in its tarball anymore.
