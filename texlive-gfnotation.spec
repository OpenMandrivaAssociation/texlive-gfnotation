Name:		texlive-gfnotation
Version:	37156
Release:	2
Summary:	Typeset Gottlob Frege's notation in plain TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gfnotation
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfnotation.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfnotation.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package implements macros for plain TeX to typeset the
notation invented by Gottlob Frege in 1879 for his books
"Begriffsschrift" and "Grundgesetze der Arithmetik" (two
volumes). The output styles of both books are supported.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/plain/gfnotation
%doc %{_texmfdistdir}/doc/plain/gfnotation

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
