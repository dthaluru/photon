Summary:	A portable, high level programming interface to various calling conventions
Name:		libffi
Version:	3.2.1
Release:	1%{?dist}
License:	BSD
URL:		http://sourceware.org/libffi/
Group:		System Environment/GeneralLibraries
Vendor:		VMware, Inc.
Distribution: 	Photon
Source0:	ftp://sourceware.org/pub/libffi/%{name}-%{version}.tar.gz
%define sha1 libffi=280c265b789e041c02e5c97815793dfc283fb1e6
Provides:	pkgconfig(libffi)
%description
The libffi library provides a portable, high level programming interface
to various calling conventions. This allows a programmer to call any 
function specified by a call interface description at run time.
%prep
%setup -q
%build
sed -e '/^includesdir/ s:$(libdir)/@PACKAGE_NAME@-@PACKAGE_VERSION@/include:$(includedir):' \
    -i include/Makefile.in &&
sed -e '/^includedir/ s:${libdir}/@PACKAGE_NAME@-@PACKAGE_VERSION@/include:@includedir@:' \
    -e 's/^Cflags: -I${includedir}/Cflags:/' \
    -i libffi.pc.in        &&
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--disable-static
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -D -m644 LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE
%ifarch x86_64
find %{buildroot}/%{_lib64dir} -name '*.la' -delete
%else
find %{buildroot}/%{_libdir} -name '*.la' -delete
%endif
rm -rf %{buildroot}/%{_infodir}
%{_fixperms} %{buildroot}/*
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%clean
rm -rf %{buildroot}/*
%files
%defattr(-,root,root)
%ifarch x86_64
%{_lib64dir}/*.so*
%else
%{_libdir}/*.so*
%endif
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datarootdir}/licenses/libffi/LICENSE
%{_mandir}/man3/*
%changelog
* 	Fri Jan 15 2016 Xiaolin Li <xiaolinl@vmware.com> 3.2.1-1
- 	Updated to version 3.2.1
*	Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 3.1-1
-	Initial build.	First version
