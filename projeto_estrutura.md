# Estrutura do Projeto: forest-portal

Este documento descreve a hierarquia de pastas e arquivos para análise de contexto.

```text
forest-portal/
├── doc/
│   └── supabase/ [conteúdo omitido]
├── public/ [conteúdo omitido]
├── src/
│   ├── app/
│   │   ├── (marketing)/
│   │   │   └── page.tsx
│   │   ├── actions/
│   │   │   └── profile.ts
│   │   ├── api/
│   │   │   └── auth/
│   │   │       ├── login/
│   │   │       │   └── route.ts
│   │   │       └── signup/
│   │   │           └── route.ts
│   │   ├── auth/
│   │   │   └── callback/
│   │   │       └── route.ts
│   │   ├── commodities/
│   │   │   └── page.tsx
│   │   ├── education/
│   │   │   └── page.tsx
│   │   ├── explore/
│   │   │   └── page.tsx
│   │   ├── join/
│   │   │   └── page.tsx
│   │   ├── open-data/
│   │   │   └── page.tsx
│   │   ├── reports/
│   │   │   └── page.tsx
│   │   ├── settings/
│   │   │   └── page.tsx
│   │   ├── favicon.ico
│   │   ├── globals.css
│   │   └── layout.tsx
│   ├── components/
│   │   ├── auth/
│   │   │   ├── AuthForm.tsx
│   │   │   └── AuthModal.tsx
│   │   ├── layout/
│   │   │   ├── Footer.tsx
│   │   │   ├── Header.tsx
│   │   │   └── SidebarSheet.tsx
│   │   ├── settings/
│   │   │   └── ProfileForm.tsx
│   │   └── ui/
│   │       ├── Button.tsx
│   │       ├── LanguageSwitcher.tsx
│   │       └── Modal.tsx
│   ├── hooks/
│   │   └── useSupabaseUser.ts
│   ├── i18n/
│   │   ├── dictionaries.ts
│   │   └── I18nProvider.tsx
│   ├── lib/
│   │   ├── supabase/
│   │   │   ├── admin.ts
│   │   │   ├── client.ts
│   │   │   ├── middleware.ts
│   │   │   └── server.ts
│   │   ├── cn.ts
│   │   └── database.types.ts
│   └── middleware.ts
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
