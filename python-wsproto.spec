# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-wsproto
Epoch: 100
Version: 1.0.0
Release: 1%{?dist}
BuildArch: noarch
Summary: WebSockets state-machine based protocol implementation
License: MIT
URL: https://github.com/python-hyper/wsproto/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This repository contains a pure-Python implementation of a WebSocket
protocol stack. It’s written from the ground up to be embeddable in
whatever program you choose to use, ensuring that you can communicate
via WebSockets, as defined in RFC6455, regardless of your programming
paradigm.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-wsproto
Summary: WebSockets state-machine based protocol implementation
Requires: python3
Requires: python3-dataclasses
Requires: python3-h11 >= 0.9.0
Provides: python3-wsproto = %{epoch}:%{version}-%{release}
Provides: python3dist(wsproto) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-wsproto = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(wsproto) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-wsproto = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(wsproto) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-wsproto
This repository contains a pure-Python implementation of a WebSocket
protocol stack. It’s written from the ground up to be embeddable in
whatever program you choose to use, ensuring that you can communicate
via WebSockets, as defined in RFC6455, regardless of your programming
paradigm.

%files -n python%{python3_version_nodots}-wsproto
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-wsproto
Summary: WebSockets state-machine based protocol implementation
Requires: python3
Requires: python3-dataclasses
Requires: python3-h11 >= 0.9.0
Provides: python3-wsproto = %{epoch}:%{version}-%{release}
Provides: python3dist(wsproto) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-wsproto = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(wsproto) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-wsproto = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(wsproto) = %{epoch}:%{version}-%{release}

%description -n python3-wsproto
This repository contains a pure-Python implementation of a WebSocket
protocol stack. It’s written from the ground up to be embeddable in
whatever program you choose to use, ensuring that you can communicate
via WebSockets, as defined in RFC6455, regardless of your programming
paradigm.

%files -n python3-wsproto
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-wsproto
Summary: WebSockets state-machine based protocol implementation
Requires: python3
Requires: python3-dataclasses
Requires: python3-h11 >= 0.9.0
Provides: python3-wsproto = %{epoch}:%{version}-%{release}
Provides: python3dist(wsproto) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-wsproto = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(wsproto) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-wsproto = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(wsproto) = %{epoch}:%{version}-%{release}

%description -n python3-wsproto
This repository contains a pure-Python implementation of a WebSocket
protocol stack. It’s written from the ground up to be embeddable in
whatever program you choose to use, ensuring that you can communicate
via WebSockets, as defined in RFC6455, regardless of your programming
paradigm.

%files -n python3-wsproto
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
