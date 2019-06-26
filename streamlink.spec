#
# spec file for package streamlink
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           streamlink
Version:	1.1.1
Release:        3
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
Requires:       python3-pycryptodome
Requires:       python-requests >= 1.0
Requires:       python3-pysocks
Requires:       python-websocket-client

Requires: mpv
Suggests: vlc
Suggests: mplayer

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

%py3_build

%install

%py3_install


#find %{buildroot}{%{python3_sitelib},%{python_sitelib}} -type f -name '*.py' | while read py; do
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
%{python3_sitelib}/%{name}*/
