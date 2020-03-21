#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Markdown and reStructuredText in a single file
Summary(pl.UTF-8):	Markdown i reStructuredText w pojedynczym pliku
Name:		python-m2r
Version:	0.2.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/m2r/
Source0:	https://files.pythonhosted.org/packages/source/m/m2r/m2r-%{version}.tar.gz
# Source0-md5:	8bdb45c19e2b59bb5ffb9a0348e81ad8
URL:		https://pypi.org/project/m2r/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-docutils
BuildRequires:	python-mistune
BuildRequires:	python-mock
BuildRequires:	python-pygments
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-docutils
BuildRequires:	python3-mistune
BuildRequires:	python3-pygments
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
M2R converts a markdown file including reStructuredText (rst) markups
to a valid rst format.

%description -l pl.UTF-8
M2R konwertuje plik markdown zawierający znaczniki reStructuredText
(rst) na poprawny format rst.

%package -n python3-m2r
Summary:	Markdown and reStructuredText in a single file
Summary(pl.UTF-8):	Markdown i reStructuredText w pojedynczym pliku
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-m2r
M2R converts a markdown file including reStructuredText (rst) markups
to a valid rst format.

%description -n python3-m2r -l pl.UTF-8
M2R konwertuje plik markdown zawierający znaczniki reStructuredText
(rst) na poprawny format rst.

%prep
%setup -q -n m2r-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/m2r{,-2}

%py_postclean
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/m2r{,-3}
ln -snf m2r-3 $RPM_BUILD_ROOT%{_bindir}/m2r
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE README.md
%attr(755,root,root) %{_bindir}/m2r-2
%{py_sitescriptdir}/m2r.py[co]
%{py_sitescriptdir}/m2r-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-m2r
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE README.md
%attr(755,root,root) %{_bindir}/m2r
%attr(755,root,root) %{_bindir}/m2r-3
%{py3_sitescriptdir}/m2r.py
%{py3_sitescriptdir}/__pycache__/m2r.cpython-*.py[co]
%{py3_sitescriptdir}/m2r-%{version}-py*.egg-info
%endif
