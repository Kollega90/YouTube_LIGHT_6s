# YouTube LIGHT 6s v1

Target:
- iPhone 6s
- iOS 15
- YouTube 20.21.6
- YTLite 5.2b4

LIGHT profile:
- YTLite core
- YouPiP
- Return YouTube Dislikes
- built-in YTLite features such as SponsorBlock/ad-related controls where supported
- YTUHD OFF
- YouQuality OFF
- YTABConfig OFF
- DontEatMyContent OFF

## Windows — кратко

1. Создай бесплатный аккаунт на GitHub.
2. Создай новый repository и загрузи содержимое этого ZIP.
3. Открой `Settings -> Actions -> General` и разреши Actions с записью в repository.
4. Открой `Actions -> Build YouTube LIGHT 6s v1`.
5. Нажми `Run workflow`.
6. В `ipa_url` вставь ПРЯМУЮ ссылку на твой decrypted YouTube 20.21.6 IPA.
7. Оставь `v5.2b4`.
8. Запусти workflow.
9. После завершения IPA будет в `Artifacts` и в `Releases`.

Важно:
- URL должен отдавать сам `.ipa`, а не страницу скачивания.
- Сам исходный IPA не включён в этот ZIP.
- Сборка выполняется на macOS runner GitHub, поэтому Mac/Windows toolchain локально не нужен.

Официальный YTLite указывает YouTube 20.21.6 как совместимый вариант для iOS 15 и GitHub Actions как способ сборки IPA.
