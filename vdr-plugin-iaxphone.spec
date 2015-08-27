%define plugin	iaxphone

Summary:	VDR plugin: Place voip phone calls
Name:		vdr-plugin-%plugin
Version:	0.0.4
Release:	21
Group:		Video
License:	GPL
URL:		http://ventoso.org/luca/vdr/
Source:		http://ventoso.org/luca/vdr/vdr-%plugin-%{version}.tgz
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
%setup -q -n %plugin-%{version}
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
%doc README HISTORY



