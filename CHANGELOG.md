# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

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
