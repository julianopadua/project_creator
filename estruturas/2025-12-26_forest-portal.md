# Estrutura do Projeto: forest-portal

Gerado em: 26/12/2025 09:48:08
Este documento descreve a hierarquia de pastas e arquivos.

```text
forest-portal/
├── doc
│   └── supabase
│       └── docSQL.md
├── public
│   ├── favicon_logo
│   │   ├── android-chrome-192x192.png
│   │   ├── android-chrome-512x512.png
│   │   ├── apple-touch-icon.png
│   │   ├── favicon-16x16.png
│   │   ├── favicon-32x32.png
│   │   ├── favicon.ico
│   │   └── site.webmanifest
│   ├── images
│   │   └── logos
│   │       ├── 001-logo.png
│   │       ├── 001-wlogo.png
│   │       ├── 002-big-logo.png
│   │       ├── 002-wbig-logo.png
│   │       ├── 003-just-words-logo.png
│   │       ├── 004-image-above-logo.png
│   │       └── 005-plain-text-logo.png
│   ├── file.svg
│   ├── globe.svg
│   ├── next.svg
│   ├── vercel.svg
│   └── window.svg
├── src
│   ├── app
│   │   ├── (marketing)
│   │   │   └── page.tsx
│   │   ├── actions
│   │   │   └── profile.ts
│   │   ├── api
│   │   │   └── auth
│   │   │       ├── login
│   │   │       │   └── route.ts
│   │   │       └── signup
│   │   │           └── route.ts
│   │   ├── auth
│   │   │   └── callback
│   │   │       └── route.ts
│   │   ├── commodities
│   │   │   └── page.tsx
│   │   ├── education
│   │   │   └── page.tsx
│   │   ├── explore
│   │   │   └── page.tsx
│   │   ├── join
│   │   │   └── page.tsx
│   │   ├── open-data
│   │   │   └── page.tsx
│   │   ├── reports
│   │   │   └── page.tsx
│   │   ├── settings
│   │   │   └── page.tsx
│   │   ├── favicon.ico
│   │   ├── globals.css
│   │   └── layout.tsx
│   ├── components
│   │   ├── auth
│   │   │   ├── AuthForm.tsx
│   │   │   └── AuthModal.tsx
│   │   ├── layout
│   │   │   ├── Footer.tsx
│   │   │   ├── Header.tsx
│   │   │   └── SidebarSheet.tsx
│   │   ├── settings
│   │   │   └── ProfileForm.tsx
│   │   └── ui
│   │       ├── Button.tsx
│   │       ├── LanguageSwitcher.tsx
│   │       └── Modal.tsx
│   ├── hooks
│   │   └── useSupabaseUser.ts
│   ├── i18n
│   │   ├── dictionaries.ts
│   │   └── I18nProvider.tsx
│   ├── lib
│   │   ├── supabase
│   │   │   ├── admin.ts
│   │   │   ├── client.ts
│   │   │   ├── middleware.ts
│   │   │   └── server.ts
│   │   ├── cn.ts
│   │   └── database.types.ts
│   └── middleware.ts
├── .env.local
├── .gitignore
├── eslint.config.mjs
├── next-env.d.ts
├── next.config.ts
├── package-lock.json
├── package.json
├── postcss.config.mjs
├── README.md
└── tsconfig.json
```
