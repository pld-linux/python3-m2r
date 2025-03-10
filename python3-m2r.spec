#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Markdown and reStructuredText in a single file
Summary(pl.UTF-8):	Markdown i reStructuredText w pojedynczym pliku
Name:		python3-m2r
Version:	0.3.1
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/m2r/
Source0:	https://files.pythonhosted.org/packages/source/m/m2r/m2r-%{version}.tar.gz
# Source0-md5:	255d080f56eb3d3a82d95194850c99c3
URL:		https://pypi.org/project/m2r/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-docutils
BuildRequires:	python3-mistune < 2
BuildRequires:	python3-pygments
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
M2R converts a markdown file including reStructuredText (rst) markups
to a valid rst format.

%description -l pl.UTF-8
M2R konwertuje plik markdown zawierający znaczniki reStructuredText
(rst) na poprawny format rst.

%prep
%setup -q -n m2r-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/m2r{,-3}
ln -snf m2r-3 $RPM_BUILD_ROOT%{_bindir}/m2r

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE README.md
%attr(755,root,root) %{_bindir}/m2r
%attr(755,root,root) %{_bindir}/m2r-3
%{py3_sitescriptdir}/m2r.py
%{py3_sitescriptdir}/__pycache__/m2r.cpython-*.py[co]
%{py3_sitescriptdir}/m2r-%{version}-py*.egg-info
