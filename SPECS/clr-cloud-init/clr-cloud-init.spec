Name:       clr-cloud-init
Version:    17
Release:    1%{?dist}
URL:        https://urldefense.proofpoint.com/v2/url?u=https-3A__github.com_clearlinux_clr-2Dcloud-2Dinit&d=BQIBaQ&c=Sqcl0Ez6M0X8aeM67LKIiDJAXVeAw-YihVMNtXt-uEs&r=lJehF0zMbgI7LaFzeIx1dblW0kHJxqAC0zgmDVHtVtY&m=lObBZLDutcx5xl-wbESfXUWZGnBkwCfkGSH4X4Yqvms&s=xdZOdADkQlzKwLFtIBUb5dQe7ghE6RrHr9X26CZwTDc&e=
Source0:    https://urldefense.proofpoint.com/v2/url?u=https-3A__github.com_clearlinux_clr-2Dcloud-2Dinit_releases_download_v-25&d=BQIBaQ&c=Sqcl0Ez6M0X8aeM67LKIiDJAXVeAw-YihVMNtXt-uEs&r=lJehF0zMbgI7LaFzeIx1dblW0kHJxqAC0zgmDVHtVtY&m=lObBZLDutcx5xl-wbESfXUWZGnBkwCfkGSH4X4Yqvms&s=NuzvcHMHgEXychg0np2EOm9NnAlScnUeTPKlJE6Mq4I&e= {version}/%{name}-%{version}.tar.xz
%define sha1 clr-cloud-init=6c82172c50218cde36a4e569e42e280aec5b4a32
Patch0:        clr-cloud-init-werror.patch
Summary:    A cloud-init implementation in C.
Group:        Development/Tools
License:    GPL-3.0
BuildRequires:    e2fsprogs-devel
BuildRequires:    shadow
BuildRequires:    check
BuildRequires:    glib-devel
BuildRequires:    json-glib-devel
BuildRequires:    curl
BuildRequires:    parted
BuildRequires:    libyaml-devel
BuildRequires:    systemd

%description
A cloud-init for Clear Linux* Project for Intel Architecture.

%prep
%setup -q -n clr-cloud-init-17
%patch0 -p1

%build
autoreconf -vif
%configure --disable-static
make V=1 CFLAGS="%{optflags}" %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%defattr(-,root,root,-)
%{_bindir}/cloud-init
/lib/systemd/system/cloud-init.service
/lib/systemd/system/multi-user.target.wants/cloud-init.service
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
