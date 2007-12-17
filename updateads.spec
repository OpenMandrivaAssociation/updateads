Summary:	Update BIND ad server listings
Name:		updateads
Version:	1.0
Release:	%mkrel 1
License:	BSD-like
Group:		Monitoring
URL:		http://prefetch.net/code/updateads.pl.html
Source0:	http://prefetch.net/code/updateads.pl.bz2
Requires:	bind
BuildArch:	noarch

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
