Summary: Library for using OBEX
Name: openobex
Version: 1.4
Release: 7%{?dist}
License: GPLv2+ and LGPLv2+
Group: System Environment/Libraries
URL: http://openobex.sourceforge.net
Source: http://www.kernel.org/pub/linux/bluetooth/openobex-%{version}.tar.gz
Patch: openobex-apps-flush.patch
Patch1: openobex-1.3-push.patch
Patch2: openobex-1.3-autoconf.patch
Patch3: openobex-1.3-ircp.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: autoconf >= 2.57, bluez-libs-devel, sed, libusb-devel
BuildRequires: automake autoconf libtool
ExcludeArch: s390 s390x

%description
OBEX (OBject EXchange) is a protocol usually used by various mobile
devices to exchange all kind of objects like files, pictures, calendar
entries (vCal) and business cards (vCard).  This package contains the
Open OBEX shared C library.

%package devel
Summary: Files for development of applications which will use OBEX
Group: Development/Libraries
Requires: %{name} = %{version}-%{release} 
Requires: bluez-libs-devel libusb-devel pkgconfig

%description devel
Header files for development of applications which use OpenOBEX.

%package apps
Summary: Applications for using OBEX
Group: System Environment/Libraries

%description apps
Open OBEX Applications to exchange all kind of objects like files, pictures,
calendar entries (vCal) and business cards (vCard) using the OBEX protocol.

%prep
%setup -q
%patch -p1 -b .flush
%patch1 -p1 -b .push
%patch2 -p1 -b .autoconf
%patch3 -p1 -b .ircp
autoreconf --install --force

%build
%configure --disable-static --enable-apps --enable-usb --disable-dependency-tracking
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
# we do not want .la files
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING COPYING.LIB ChangeLog README 
%{_libdir}/libopenobex*.so.*

%files devel
%defattr(-, root, root)
%{_libdir}/libopenobex*.so
%dir %{_includedir}/openobex
%{_includedir}/openobex/*.h
%{_libdir}/pkgconfig/openobex.pc

%files apps
%defattr(-, root, root)
%{_bindir}/irobex_palm3
%{_bindir}/irxfer
%{_bindir}/ircp
%{_bindir}/obex_tcp
%{_bindir}/obex_test
%{_bindir}/obex_push
%{_mandir}/man1/obex_push.1*


%changelog
* Fri Feb 26 2010 Jiri Moskovcak <jmoskovc@redhat.com> - 1.4-7
- again fixed the license tag to follow Fedora guidlines
- Related: #543948

* Fri Feb 26 2010 Jiri Moskovcak <jmoskovc@redhat.com> - 1.4-6
- really fixed license tag
- Related: #543948

* Fri Feb 26 2010 Jiri Moskovcak <jmoskovc@redhat.com> - 1.4-5
- fixed license
- Related: #543948

* Fri Jan  8 2010 Jiri Moskovcak <jmoskovc@redhat.com> - 1.4-4
- fixed source url
- Resolves: #543948

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.4-3.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov 18 2008 Jiri Moskovcak <jmoskovc@redhat.com> 1.4.1
- New upstream version
- Spec file cleanup
- Removed unneeded patches

* Thu Oct  2 2008 Jiri Moskovcak <jmoskovc>@redhat.com> 1.3.15
- rebuilt against new bluez-libs

* Thu Oct  2 2008 Jiri Moskovcak <jmoskovc@redhat.com> 1.3.14
- bump release

* Wed Jun 18 2008 Jiri Moskovcak <jmoskovc@redhat.com> 1.3-13
- fixed problem when ircp tries to write files to /
- Resolves: #451493

* Mon Jun  2 2008 Jiri Moskovcak <jmoskovc@redhat.com> - 1.3-12
- improved utf(non ascii) support
- Resolves: #430128

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3-11
- Autorebuild for GCC 4.3

* Mon Oct 29 2007 Jiri Moskovcak <jmoskovc@redhat.com> - 1.3-10
- Spec file cleanup

* Fri Oct 26 2007 Jiri Moskovcak <jmoskovc@redhat.com> - 1.3-9
- Spec file cleanup
- Fixed wrong lib path in autoconf

* Tue Sep 18 2007 Jiri Moskovcak <jmoskovc@redhat.com> - 1.3-8
- Changed sources in specfile URL to point to the right location

* Fri Aug 24 2007 Jiri Moskovcak <jmoskovc@redhat.com> - 1.3-7
- Added ipv6 support
- Resolves: #198396

* Wed Aug 22 2007 Harald Hoyer <harald@redhat.com> - 1.3-6
- changed license tag

* Fri Mar 23 2007 Harald Hoyer <harald@redhat.com> - 1.3-5
- specfile cleanup

* Wed Feb  7 2007 Harald Hoyer <harald@redhat.com> - 1.3-4
- readded obex_push

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.3-3.1
- rebuild

* Tue Jun 27 2006 Harald Hoyer <harald@redhat.com> - 1.3-3
- removed more patches

* Tue Jun 27 2006 Harald Hoyer <harald@redhat.com> - 1.3-2
- added more build requirements
- built now with enable-usb

* Fri Jun 16 2006 Harald Hoyer <harald@redhat.com> - 1.3-1
- version 1.3

* Tue Jun 13 2006 Harald Hoyer <harald@redhat.com> - 1.2-2
- more build requirements

* Tue Jun 13 2006 Harald Hoyer <harald@redhat.com> - 1.2-1
- version 1.2

* Thu Feb 16 2006 Harald Hoyer <harald@redhat.com> 1.1-1
- version 1.1

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1-4.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1-4.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon May 02 2005 Harald Hoyer <harald@redhat.com> 1.0.1-4
- added `OBEX_ServerAccept' to the exported symbols (bug rh#146353)

* Wed Mar 02 2005 Harald Hoyer <harald@redhat.com> 
- rebuilt

* Wed Feb 09 2005 Harald Hoyer <harald@redhat.com>
- rebuilt

* Mon Sep 13 2004 Harald Hoyer <harald@redhat.de> 1.0.1-1
- version 1.0.1

* Tue Jun 22 2004 Alan Cox <alan@redhat.com>
- removed now unneeded glib requirement

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Apr 19 2004 David Woodhouse <dwmw2@redhat.com> 1.0.0-5
- import for for #121271 from openobex CVS tree

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun  4 2003 Harald Hoyer <harald@redhat.de> 1.0.0-2
- excludeArch s390 s390x

* Wed Jun  4 2003 Harald Hoyer <harald@redhat.de> 1.0.0-1
- redhatified specfile
- bump to version 1.0.0

* Thu May 18 2000 Pontus Fuchs <pontus.fuchs@tactel.se>
- Initial RPM


