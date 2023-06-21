# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

### [0.4.3](https://github.com/DataShades/ckanext-flakes/compare/v0.4.2...v0.4.3) (2023-06-21)


### Features

* **test:** add FlakesFeedbackFactory ([6981fd2](https://github.com/DataShades/ckanext-flakes/commit/6981fd23b31ba895b4d68c1dbe8519eabc5735c5))

### [0.4.2](https://github.com/DataShades/ckanext-flakes/compare/v0.4.1...v0.4.2) (2023-06-21)


### Bug Fixes

* custom context is ignored during feedback creation ([77df6cf](https://github.com/DataShades/ckanext-flakes/commit/77df6cfa43d2c967976bb131bb3726cb5513c42e))

### [0.4.1](https://github.com/DataShades/ckanext-flakes/compare/v0.4.0...v0.4.1) (2023-06-11)


### Features

* override existing feedbacks via feedback_create ([f34c9c6](https://github.com/DataShades/ckanext-flakes/commit/f34c9c634e9dcd704eddc055015a8ba72b8df776))

## [0.4.0](https://github.com/DataShades/ckanext-flakes/compare/v0.3.9...v0.4.0) (2023-06-07)


### ⚠ BREAKING CHANGES

* flakes_feedback use secondary_key for multiple feedbacks per package

### Features

* flakes_feedback use secondary_key for multiple feedbacks per package ([5b3594f](https://github.com/DataShades/ckanext-flakes/commit/5b3594f6f6fd67a0827703fdd525d245c2d13561))

### [0.3.9](https://github.com/DataShades/ckanext-flakes/compare/v0.3.8...v0.3.9) (2023-04-19)


### Bug Fixes

* allow double-classes on rate widget ([8b75acb](https://github.com/DataShades/ckanext-flakes/commit/8b75acb353f9695cf6f334c02d60f5a4b3d7d184))

### [0.3.8](https://github.com/DataShades/ckanext-flakes/compare/v0.3.7...v0.3.8) (2023-04-19)


### Features

* flakes_rating allows configuring both star states ([c143d21](https://github.com/DataShades/ckanext-flakes/commit/c143d21d1f769feccb302834ab7cc86552a08e1b))


### Bug Fixes

* flakes_feedback cannot be hidden from UI ([b63b704](https://github.com/DataShades/ckanext-flakes/commit/b63b704bc6ebfbb013a55bd97379924d50ae2517))

### [0.3.7](https://github.com/DataShades/ckanext-flakes/compare/v0.3.6...v0.3.7) (2023-03-23)


### Bug Fixes

* flakes_feedback ignores delete permissions ([11de936](https://github.com/DataShades/ckanext-flakes/commit/11de9363aa307e56c7d8cbfbec7f43126739bbf0))

### [0.3.6](https://github.com/DataShades/ckanext-flakes/compare/v0.3.5...v0.3.6) (2023-03-23)


### Features

* add "delete" button to feedbacks list ([192709d](https://github.com/DataShades/ckanext-flakes/commit/192709d407863c39f253aac0530765604d2d0a55))
* add blocks to feedbacks listing ([376bb65](https://github.com/DataShades/ckanext-flakes/commit/376bb65f6b7e90d73864db89c8436f4694cc69e9))

### [0.3.5](https://github.com/DataShades/ckanext-flakes/compare/v0.3.4...v0.3.5) (2023-03-23)


### Features

* default rating widget for flakes_rating ([6db114a](https://github.com/DataShades/ckanext-flakes/commit/6db114a668d6419dfa8084b321fe5b107678d8e7))
* flakes_feedback plugin ([5c98b4e](https://github.com/DataShades/ckanext-flakes/commit/5c98b4e10853edae05bf16f68a812b327ee2ae29))


### Bug Fixes

* lookup and list do not show owned flakes ([9b3d4a8](https://github.com/DataShades/ckanext-flakes/commit/9b3d4a87736efdcb8b5e2089e3a7d3fd4e42ff7e))

### [0.3.4](https://github.com/DataShades/ckanext-flakes/compare/v0.3.3...v0.3.4) (2023-03-12)


### Bug Fixes

* search by author ignores name ([85b411c](https://github.com/DataShades/ckanext-flakes/commit/85b411c825bace3c32ddec0a73e226bb5ef0f43d))

### [0.3.3](https://github.com/DataShades/ckanext-flakes/compare/v0.3.2...v0.3.3) (2023-03-12)


### Features

* flakes_rating shows rating of multiple items ([0a2390d](https://github.com/DataShades/ckanext-flakes/commit/0a2390d46231e7d4cee460e60057d7c7849044ac))

### [0.3.2](https://github.com/DataShades/ckanext-flakes/compare/v0.3.1...v0.3.2) (2023-03-12)


### Bug Fixes

* override works with unowned flakes ([cdae07d](https://github.com/DataShades/ckanext-flakes/commit/cdae07df0330bac6a39613419f69f0f1e4720caf))

### [0.3.1](https://github.com/DataShades/ckanext-flakes/compare/v0.3.0...v0.3.1) (2023-03-12)


### Bug Fixes

* remove type annotations from schemas(v2.9 support) ([a8e309a](https://github.com/DataShades/ckanext-flakes/commit/a8e309a4c097ba6b7c44a7d3766e37e1e0cc64dd))

## [0.3.0](https://github.com/DataShades/ckanext-flakes/compare/v0.2.3...v0.3.0) (2023-03-12)


### ⚠ BREAKING CHANGES

* flake_list accepts athor_id
* flake_create(author_id=None) creates unowned flakes

### Features

* add config declarations ([6ac4bbb](https://github.com/DataShades/ckanext-flakes/commit/6ac4bbb960cc7efbcd21bfb38f967d8507dbb89d))
* flake_create(author_id=None) creates unowned flakes ([55755ce](https://github.com/DataShades/ckanext-flakes/commit/55755ce1b45f52c9fb3a1ec8713847515bedb478))
* flake_list accepts athor_id ([a385a61](https://github.com/DataShades/ckanext-flakes/commit/a385a6138c449280c7d7ba79ab4f7a9c25abf572))
* lookup unowned flakes with author_id=None ([608d0a9](https://github.com/DataShades/ckanext-flakes/commit/608d0a957dff79544fa8638305031378edc957c6))

### [0.2.3](https://github.com/DataShades/ckanext-flakes/compare/v0.2.2...v0.2.3) (2023-03-02)


### Bug Fixes

* flakes_rating error for anonymous user ([b318df1](https://github.com/DataShades/ckanext-flakes/commit/b318df1856f93c08e3f5331ae2385e5a242a3703))

### [0.2.2](https://github.com/DataShades/ckanext-flakes/compare/v0.2.1...v0.2.2) (2023-03-01)


### Features

* add types for API ([82e2cc5](https://github.com/DataShades/ckanext-flakes/commit/82e2cc5094a72f770de91537cfee768e9ec34366))
* configurable star-icon for flakes_rating ([94241ae](https://github.com/DataShades/ckanext-flakes/commit/94241ae61256092d3cad61afe2791ddb5799d92e))

### [0.2.1](https://github.com/DataShades/ckanext-flakes/compare/v0.2.0...v0.2.1) (2022-11-11)


### Bug Fixes

* ignore user when listing flakes globally ([937f959](https://github.com/DataShades/ckanext-flakes/commit/937f95972013902f7e535bfcf5e7f2f5beb97888))

## [0.2.0](https://github.com/DataShades/ckanext-flakes/compare/v0.1.0...v0.2.0) (2022-11-02)


### ⚠ BREAKING CHANGES

* flakes_rating plugin

### Features

* flakes_rating plugin ([31d313f](https://github.com/DataShades/ckanext-flakes/commit/31d313fce88398db0fde06bcec80b33e47802d13))
* model.Flake.by_name returns query ([ddbe13c](https://github.com/DataShades/ckanext-flakes/commit/ddbe13c002be779ae151dc987a1d4823fb6b3c3c))

## [0.1.0](https://github.com/DataShades/ckanext-flakes/compare/v0.0.7...v0.1.0) (2022-10-27)


### ⚠ BREAKING CHANGES

* flakes_list uses extras-dictionary as filter

### Features

* flakes_list uses extras-dictionary as filter ([700fcc8](https://github.com/DataShades/ckanext-flakes/commit/700fcc82b17cd1ef42d1ec16676a1c634b39a400))
