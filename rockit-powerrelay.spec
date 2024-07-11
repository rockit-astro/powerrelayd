Name:      rockit-powerrelay
Version:   %{_version}
Release:   1
Summary:   Power control
Url:       https://github.com/rockit-astro/powerrelayd
License:   GPL-3.0
BuildArch: noarch

%description


%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/powerrelayd/
mkdir -p %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/powerrelayd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/powerrelayd@.service %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/sting.json %{buildroot}%{_sysconfdir}/powerrelayd/
%{__install} %{_sourcedir}/10-sting-power.rules %{buildroot}%{_udevrulesdir}

%package server
Summary:  Power relay control server
Group:    Unspecified
Requires: python3-rockit-common
%description server

%files server
%defattr(0755,root,root,-)
%{_bindir}/powerrelayd
%defattr(0644,root,root,-)
%{_unitdir}/powerrelayd@.service

%package data-sting
Summary: Power relay control data for the STING telescope
Group:   Unspecified
%description data-sting

%files data-sting
%defattr(0644,root,root,-)
%{_udevrulesdir}/10-sting-power.rules
%{_sysconfdir}/powerrelayd/sting.json

%changelog
