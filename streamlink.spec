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
Version:        0.13.0
Release:        1.1
Summary:        Program to pipe streams from services into a video player
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            http://streamlink.github.io/
Source:         https://github.com/%{name}/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Recommends:     (vlc or mpv)
BuildArch:      noarch
%if 0%{?suse_version} > 1320
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel >= 3.4
BuildRequires:  python3-setuptools
Requires:       python3-iso-639
Requires:       python3-iso3166
Requires:       python3-pycryptodome
Requires:       python3-requests >= 1.0
%else
BuildRequires:  python-Sphinx
BuildRequires:  python-devel >= 2.7
BuildRequires:  python-futures
BuildRequires:  python-setuptools
BuildRequires:  python-singledispatch
Requires:       python-iso-639
Requires:       python-iso3166
Requires:       python-pycryptodome
Requires:       python-requests >= 1.0
%endif

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
%if 0%{?suse_version} > 1320
python3 setup.py build
%else
python2 setup.py build
%endif

%install
%if 0%{?suse_version} > 1320
python3 setup.py install \
%else
python2 setup.py install \
%endif
  --root=%{buildroot} \
  --prefix=%{_prefix}

find %{buildroot}{%{python3_sitelib},%{python_sitelib}} -type f -name '*.py' | while read py; do
    if [[ "$(head -c2 "$py"; echo)" == "#!" ]]; then
        chmod a+x "$py"
    else
        chmod a-x "$py"
    fi
done

%files
%license LICENSE
%doc AUTHORS CHANGELOG.md MANIFEST.in README.md
%{_bindir}/%{name}
%if 0%{?suse_version} > 1320
%{python3_sitelib}/%{name}*/
%else
%{python_sitelib}/%{name}*/
%endif

%changelog
* Sun Jun 24 2018 dmarcoux@posteo.de
- Update to version 0.13.0:
  * Initial MPEG DASH support has been added! (#1637) Many thanks to @beardypig
  * As always, a ton of plugin updates
  * Updates to our documentation (#1673)
  * Updates to our logging (#1752) as well as log --quiet options (#1744) (#1720)
  * Our release script has been updated (#1711)
  * Support for livestreams when using the --hls-duration option (#1710)
  * Allow streamlink to exit faster when using Ctrl+C (#1658)
  * Added an OpenCV Face Detection example (#1689)
- Remove streamlink-use-mpv.patch
* Tue Dec 19 2017 agraul@suse.com
- Update to version 0.9.0:
  * Updates to multiple plugins (electrecetv, tvplayer, Teve2,
    cnnturk, kanald)
- Update streamlink-use-mpv.patch
  * Refresh to apply on rebased code
* Sun Sep 17 2017 mpluskal@suse.com
- Update conditionals to resolve dependencies on Leap
* Tue Mar  7 2017 p.seiler@linuxmail.org
- update to version 0.3.2
- Added new Requirements:
  * python[3]-iso3166
  * python[3]-iso-639
  * python[3]-pycryptodome
* Wed Dec  7 2016 josipponjavic@gmail.com
- Initial package.
