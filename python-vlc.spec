%global pypi_name python_vlc

Name:           python-vlc
Version:        3.0.21203
Release:        %autorelease
Summary:        VLC Media Player binding for Python

License:        LGPL-2.0-or-later
URL:            https://wiki.videolan.org/PythonBinding
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
This package provides a python interface to control VLC Media Player.

%package -n python3-vlc
Summary:        VLC Media Player binding for Python
Requires:       vlc-cli >= 1.1.0
%{?python_provide:%python_provide python3-vlc}

%description -n python3-vlc
This package provides a python interface to control VLC Media Player.

%prep
%autosetup -n %{pypi_name}-%{version}

#fix rpmlint
%{py3_shebang_fix} vlc.py examples/*.py
# Move README.md
mv examples/video_sync/README.md .

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l vlc

#fix rpmlint
chmod +x %{buildroot}%{python3_sitelib}/vlc.py

%files -n python3-vlc -f %{pyproject_files}
%doc README.module README.md examples/
%license COPYING

%changelog
%autochangelog

