Name:           streamlink
Version:        1.7.0
Release:        2
Summary:        Program to pipe streams from services into a video player
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            http://streamlink.github.io/
Source:         https://github.com/streamlink/streamlink/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-sphinx
BuildRequires:  python-devel >= 3.4
BuildRequires:  python-setuptools
Requires:       python3-iso-639
Requires:       python3-iso3166
Requires:       python-pycryptodome
Requires:       python-requests >= 1.0
Requires:       python3-pysocks
Requires:       python-websocket-client

Requires: mpv
Recommends: vlc
Recommends: mplayer

%description
Streamlink is a CLI utility that pipes flash videos
from online streaming services to a variety of video players
such as MPV, or alternatively, a browser.
The main purpose of streamlink is to convert CPU-heavy
flash plugins to a less CPU-intensive format.
Streamlink is a fork of the livestreamer project.

%prep
%setup -q

%build

%py_build

%install

%py_install


#find %{buildroot}{%{python_sitelib},%{python_sitelib}} -type f -name '*.py' | while read py; do
#    if [[ "$(head -c2 "$py"; echo)" == "#!" ]]; then
#        chmod a+x "$py"
#    else
#        chmod a-x "$py"
#    fi
#done

%files
%license LICENSE
%doc AUTHORS CHANGELOG.md MANIFEST.in README.md
%{_bindir}/%{name}
%{python_sitelib}/%{name}*/
