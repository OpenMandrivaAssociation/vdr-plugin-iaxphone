%define plugin	iaxphone

Summary:	VDR plugin: Place voip phone calls
Name:		vdr-plugin-%plugin
Version:	0.0.4
Release:	19
Group:		Video
License:	GPL
URL:		http://ventoso.org/luca/vdr/
Source:		http://ventoso.org/luca/vdr/vdr-%plugin-%version.tar.bz2
Patch0:		iaxphone-0.0.4-i18n-1.6.patch
Patch1:		iaxphone-system-iaxclient.patch
Patch2:		iaxphone-new-iaxclient.patch
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	iaxclient-devel
Requires:	vdr-abi = %vdr_abi

%description
This plugin is a very simple (read: not very featureful and hopefully with
an high WAF ;-) softphone using the iax protocol (asterisk server).
It uses the iaxclient library (http://iaxclient.sourceforge.net) to handle
every details of the call, so the plugin is just an user interface.
It needs a free (i.e that isn't used by something else, like a softdevice
plugin), full-duplex sound card.

%prep
%setup -q -n %plugin-%version
rm -rf iaxclient
%patch0 -p1
%patch1 -p1
%patch2 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.4-17mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Sat Mar 21 2009 Anssi Hannula <anssi@mandriva.org> 0.0.4-16mdv2009.1
+ Revision: 359838
- fix build with recent iaxclient (new-iaxclient.patch)
- use system libiaxclient (system-iaxclient.patch)
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.4-15mdv2009.0
+ Revision: 197937
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.4-14mdv2009.0
+ Revision: 197679
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.4-13mdv2008.1
+ Revision: 145103
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4-12mdv2008.1
+ Revision: 103143
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4-11mdv2008.0
+ Revision: 50008
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4-10mdv2008.0
+ Revision: 42094
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4-9mdv2008.0
+ Revision: 22694
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4-8mdv2007.0
+ Revision: 90931
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4-7mdv2007.1
+ Revision: 74026
- rebuild for new vdr
- Import vdr-plugin-iaxphone

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4-6mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4-5mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4-4mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4-3mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4-2mdv2007.0
- rebuild for new vdr

* Tue Jun 06 2006 Anssi Hannula <anssi@mandriva.org> 0.0.4-1mdv2007.0
- initial Mandriva release

