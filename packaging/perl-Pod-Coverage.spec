#
# spec file for package perl-Pod-Coverage
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Pod-Coverage
Version:        0.22
Release:        0
License:        GPL-1.0+ or Artistic-1.0
%define cpan_name Pod-Coverage
Summary:        Checks if the documentation of a module is comprehensive
Url:            http://search.cpan.org/dist/Pod-Coverage/
Group:          Development/Libraries/Perl
Source:         http://www.cpan.org/authors/id/R/RC/RCLAMP/%{cpan_name}-%{version}.tar.gz
Source1001: 	perl-Pod-Coverage.manifest
BuildRequires:  perl
BuildRequires:  perl(Devel::Symdump) >= 2.01
BuildRequires:  perl-macros
Requires:       perl(Devel::Symdump) >= 2.01
BuildArch:      noarch

%description
Developers hate writing documentation. They'd hate it even more if their
computer tattled on them, but maybe they'll be even more thankful in the
long run. Even if not, _perlmodstyle_ tells you to, so you must obey.

This module provides a mechanism for determining if the pod for a given
module is comprehensive.

It expects to find either a '=head(n>1)' or an '=item' block documenting a
subroutine.

Consider: # an imaginary Foo.pm package Foo;

 =item foo

 The foo sub

 = cut

 sub foo {}
 sub bar {}

 1;
 __END__

In this example 'Foo::foo' is covered, but 'Foo::bar' is not, so the 'Foo'
package is only 50% (0.5) covered

%prep
%setup -q -n %{cpan_name}-%{version}
cp %{SOURCE1001} .

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%manifest %{name}.manifest
%defattr(-,root,root,755)

%changelog
