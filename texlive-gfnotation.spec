%global tl_name gfnotation
%global tl_revision 37156

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.9
Release:	%{tl_revision}.1
Summary:	Typeset Gottlob Freges notation in plain TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/gfnotation
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfnotation.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfnotation.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package implements macros for plain TeX to typeset the notation
invented by Gottlob Frege in 1879 for his books "Begriffsschrift" and
"Grundgesetze der Arithmetik" (two volumes). The output styles of both
books are supported.

