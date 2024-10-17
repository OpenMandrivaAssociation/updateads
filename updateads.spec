Summary:	Update BIND ad server listings
Name:		updateads
Version:	1.0
Release:	6
License:	BSD-like
Group:		Monitoring
URL:		https://prefetch.net/code/updateads.pl.html
Source0:	http://prefetch.net/code/updateads.pl.bz2
Requires:	bind
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
updatedads.pl is a Perl script that can be used to retrieve and format the
latest list of well known ad servers for placement in a BIND zone file.

%prep

%setup -q -c -T
bzcat %{SOURCE0} > %{name}

%build

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/%{name}


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0-5mdv2010.0
+ Revision: 434565
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0-4mdv2009.0
+ Revision: 261777
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0-3mdv2009.0
+ Revision: 255178
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0-1mdv2008.1
+ Revision: 140925
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2008.0
+ Revision: 83828
- Import updateads



* Tue Aug 22 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2007.0
- initial Mandriva package
