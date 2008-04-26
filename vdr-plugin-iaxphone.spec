
%define plugin	iaxphone
%define name	vdr-plugin-%plugin
%define version	0.0.4
%define rel	14

Summary:	VDR plugin: Place voip phone calls
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://ventoso.org/luca/vdr/
Source:		http://ventoso.org/luca/vdr/vdr-%plugin-%version.tar.bz2
Patch0:		iaxphone-0.0.4-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
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
perl -pi -e "s/CFLAGS=/CFLAGS= %optflags -fPIC/" iaxclient/lib/Makefile
%patch0 -p1
%vdr_plugin_prep

%build
%make -C iaxclient/lib libiaxclient.a
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


