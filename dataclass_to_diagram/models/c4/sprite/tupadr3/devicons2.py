"""devicons lib."""

from ...base import BaseSprite


class Devicons2(BaseSprite):
    """Библиотека спрайтов."""

    def include_statements_for_sprite(self) -> set[str]:
        """Возвращает include для спрайтов."""
        return {
            "!include <tupadr3/common>",
            "!include <tupadr3/devicons2/{0}>".format(self.value),
        }

    aarch64 = "aarch64"
    aftereffects = "aftereffects"
    amazonwebservices_original = "amazonwebservices_original"
    amazonwebservices_wordmark = "amazonwebservices_wordmark"
    android = "android"
    android_wordmark = "android_wordmark"
    angularjs = "angularjs"
    angularjs_wordmark = "angularjs_wordmark"
    apache = "apache"
    apache_line = "apache_line"
    apache_line_wordmark = "apache_line_wordmark"
    apache_wordmark = "apache_wordmark"
    appcelerator_original = "appcelerator_original"
    appcelerator_wordmark = "appcelerator_wordmark"
    apple_original = "apple_original"
    appwrite = "appwrite"
    appwrite_wordmark = "appwrite_wordmark"
    atom_original = "atom_original"
    atom_original_wordmark = "atom_original_wordmark"
    babel = "babel"
    backbonejs = "backbonejs"
    backbonejs_wordmark = "backbonejs_wordmark"
    bash = "bash"
    behance = "behance"
    behance_wordmark = "behance_wordmark"
    bitbucket_original = "bitbucket_original"
    bitbucket_original_wordmark = "bitbucket_original_wordmark"
    bootstrap = "bootstrap"
    bootstrap_wordmark = "bootstrap_wordmark"
    bower = "bower"
    bower_line = "bower_line"
    bower_line_wordmark = "bower_line_wordmark"
    bower_wordmark = "bower_wordmark"
    bulma = "bulma"
    c = "c"
    c_line = "c_line"
    cakephp = "cakephp"
    cakephp_wordmark = "cakephp_wordmark"
    ceylon = "ceylon"
    chrome = "chrome"
    chrome_wordmark = "chrome_wordmark"
    circleci = "circleci"
    circleci_wordmark = "circleci_wordmark"
    clojure_line = "clojure_line"
    clojurescript = "clojurescript"
    codecov = "codecov"
    codeigniter = "codeigniter"
    codeigniter_wordmark = "codeigniter_wordmark"
    codepen = "codepen"
    codepen_original_wordmark = "codepen_original_wordmark"
    coffeescript_original = "coffeescript_original"
    coffeescript_original_wordmark = "coffeescript_original_wordmark"
    composer_line = "composer_line"
    composer_line_wordmark = "composer_line_wordmark"
    confluence_original = "confluence_original"
    confluence_original_wordmark = "confluence_original_wordmark"
    couchdb = "couchdb"
    couchdb_wordmark = "couchdb_wordmark"
    cplusplus = "cplusplus"
    cplusplus_line = "cplusplus_line"
    crystal_original = "crystal_original"
    crystal_original_wordmark = "crystal_original_wordmark"
    csharp = "csharp"
    csharp_line = "csharp_line"
    css3 = "css3"
    css3_wordmark = "css3_wordmark"
    cucumber = "cucumber"
    cucumber_wordmark = "cucumber_wordmark"
    d3js = "d3js"
    d3js_original = "d3js_original"
    dart = "dart"
    dart_wordmark = "dart_wordmark"
    debian = "debian"
    debian_wordmark = "debian_wordmark"
    devicon = "devicon"
    devicon_wordmark = "devicon_wordmark"
    digitalocean = "digitalocean"
    digitalocean_wordmark = "digitalocean_wordmark"
    django = "django"
    django_line = "django_line"
    docker = "docker"
    docker_wordmark = "docker_wordmark"
    doctrine = "doctrine"
    doctrine_line = "doctrine_line"
    doctrine_line_wordmark = "doctrine_line_wordmark"
    doctrine_wordmark = "doctrine_wordmark"
    dot_net = "dot_net"
    dot_net_wordmark = "dot_net_wordmark"
    dotnetcore = "dotnetcore"
    drupal = "drupal"
    drupal_wordmark = "drupal_wordmark"
    electron_original = "electron_original"
    electron_original_wordmark = "electron_original_wordmark"
    eleventy = "eleventy"
    elixir = "elixir"
    elixir_wordmark = "elixir_wordmark"
    elm = "elm"
    elm_wordmark = "elm_wordmark"
    embeddedc = "embeddedc"
    embeddedc_wordmark = "embeddedc_wordmark"
    ember_original_wordmark = "ember_original_wordmark"
    erlang = "erlang"
    erlang_wordmark = "erlang_wordmark"
    express_original = "express_original"
    express_original_wordmark = "express_original_wordmark"
    facebook = "facebook"
    figma = "figma"
    firebase = "firebase"
    firebase_wordmark = "firebase_wordmark"
    firefox = "firefox"
    firefox_wordmark = "firefox_wordmark"
    flask_original = "flask_original"
    flask_original_wordmark = "flask_original_wordmark"
    flutter = "flutter"
    foundation = "foundation"
    foundation_wordmark = "foundation_wordmark"
    fsharp = "fsharp"
    gatling = "gatling"
    gatling_wordmark = "gatling_wordmark"
    gatsby = "gatsby"
    gatsby_wordmark = "gatsby_wordmark"
    gimp = "gimp"
    git = "git"
    git_wordmark = "git_wordmark"
    github_original = "github_original"
    github_original_wordmark = "github_original_wordmark"
    gitlab = "gitlab"
    gitlab_wordmark = "gitlab_wordmark"
    gitter = "gitter"
    gitter_wordmark = "gitter_wordmark"
    go = "go"
    go_line = "go_line"
    godot = "godot"
    godot_wordmark = "godot_wordmark"
    google = "google"
    google_wordmark = "google_wordmark"
    googlecloud = "googlecloud"
    googlecloud_wordmark = "googlecloud_wordmark"
    gradle = "gradle"
    gradle_wordmark = "gradle_wordmark"
    grails = "grails"
    graphql = "graphql"
    graphql_wordmark = "graphql_wordmark"
    groovy = "groovy"
    grunt = "grunt"
    grunt_line = "grunt_line"
    grunt_line_wordmark = "grunt_line_wordmark"
    grunt_wordmark = "grunt_wordmark"
    gulp = "gulp"
    handlebars = "handlebars"
    handlebars_wordmark = "handlebars_wordmark"
    haskell = "haskell"
    haskell_wordmark = "haskell_wordmark"
    haxe = "haxe"
    heroku = "heroku"
    heroku_line = "heroku_line"
    heroku_line_wordmark = "heroku_line_wordmark"
    heroku_wordmark = "heroku_wordmark"
    html5 = "html5"
    html5_wordmark = "html5_wordmark"
    ie10_original = "ie10_original"
    illustrator = "illustrator"
    illustrator_line = "illustrator_line"
    index = "index"
    inkscape = "inkscape"
    inkscape_wordmark = "inkscape_wordmark"
    intellij = "intellij"
    intellij_wordmark = "intellij_wordmark"
    ionic_original = "ionic_original"
    ionic_original_wordmark = "ionic_original_wordmark"
    jasmine = "jasmine"
    jasmine_wordmark = "jasmine_wordmark"
    java = "java"
    java_wordmark = "java_wordmark"
    javascript = "javascript"
    jeet = "jeet"
    jeet_wordmark = "jeet_wordmark"
    jenkins = "jenkins"
    jenkins_line = "jenkins_line"
    jest = "jest"
    jetbrains = "jetbrains"
    jquery = "jquery"
    jquery_wordmark = "jquery_wordmark"
    julia = "julia"
    julia_wordmark = "julia_wordmark"
    jupyter = "jupyter"
    jupyter_wordmark = "jupyter_wordmark"
    karma = "karma"
    knockout_wordmark = "knockout_wordmark"
    kotlin = "kotlin"
    kotlin_wordmark = "kotlin_wordmark"
    krakenjs = "krakenjs"
    krakenjs_wordmark = "krakenjs_wordmark"
    kubernetes = "kubernetes"
    kubernetes_wordmark = "kubernetes_wordmark"
    labview = "labview"
    labview_wordmark = "labview_wordmark"
    laravel = "laravel"
    laravel_wordmark = "laravel_wordmark"
    less_wordmark = "less_wordmark"
    linkedin = "linkedin"
    linkedin_wordmark = "linkedin_wordmark"
    linux = "linux"
    lua = "lua"
    lua_wordmark = "lua_wordmark"
    magento_line = "magento_line"
    magento_original = "magento_original"
    magento_original_wordmark = "magento_original_wordmark"
    materialui = "materialui"
    matlab = "matlab"
    matlab_line = "matlab_line"
    meteor = "meteor"
    meteor_wordmark = "meteor_wordmark"
    microsoftsqlserver = "microsoftsqlserver"
    microsoftsqlserver_wordmark = "microsoftsqlserver_wordmark"
    minitab = "minitab"
    mocha = "mocha"
    modx = "modx"
    modx_wordmark = "modx_wordmark"
    mongodb = "mongodb"
    mongodb_wordmark = "mongodb_wordmark"
    moodle = "moodle"
    moodle_wordmark = "moodle_wordmark"
    mysql = "mysql"
    mysql_wordmark = "mysql_wordmark"
    nestjs = "nestjs"
    nestjs_wordmark = "nestjs_wordmark"
    nextjs_line = "nextjs_line"
    nextjs_original = "nextjs_original"
    nextjs_original_wordmark = "nextjs_original_wordmark"
    nginx_original = "nginx_original"
    nixos = "nixos"
    nixos_wordmark = "nixos_wordmark"
    nodejs = "nodejs"
    nodejs_wordmark = "nodejs_wordmark"
    nodewebkit = "nodewebkit"
    nodewebkit_line = "nodewebkit_line"
    nodewebkit_line_wordmark = "nodewebkit_line_wordmark"
    nodewebkit_wordmark = "nodewebkit_wordmark"
    npm_original_wordmark = "npm_original_wordmark"
    objectivec = "objectivec"
    ocaml = "ocaml"
    ocaml_wordmark = "ocaml_wordmark"
    oracle_original = "oracle_original"
    perl = "perl"
    phalcon = "phalcon"
    phoenix = "phoenix"
    phoenix_wordmark = "phoenix_wordmark"
    photoshop = "photoshop"
    photoshop_line = "photoshop_line"
    php = "php"
    phpstorm = "phpstorm"
    phpstorm_wordmark = "phpstorm_wordmark"
    postgresql = "postgresql"
    postgresql_wordmark = "postgresql_wordmark"
    premierepro = "premierepro"
    protractor = "protractor"
    protractor_wordmark = "protractor_wordmark"
    pycharm = "pycharm"
    pycharm_wordmark = "pycharm_wordmark"
    python = "python"
    python_wordmark = "python_wordmark"
    r = "r"
    r_original = "r_original"
    rails = "rails"
    rails_wordmark = "rails_wordmark"
    raspberrypi_line = "raspberrypi_line"
    raspberrypi_line_wordmark = "raspberrypi_line_wordmark"
    react_original = "react_original"
    react_original_wordmark = "react_original_wordmark"
    redhat = "redhat"
    redhat_wordmark = "redhat_wordmark"
    redis = "redis"
    redis_wordmark = "redis_wordmark"
    redux_original = "redux_original"
    rocksdb = "rocksdb"
    rstudio = "rstudio"
    ruby = "ruby"
    ruby_wordmark = "ruby_wordmark"
    rubymine = "rubymine"
    rubymine_wordmark = "rubymine_wordmark"
    rust = "rust"
    safari = "safari"
    safari_line = "safari_line"
    safari_line_wordmark = "safari_line_wordmark"
    safari_wordmark = "safari_wordmark"
    salesforce = "salesforce"
    sass_original = "sass_original"
    scala = "scala"
    scala_wordmark = "scala_wordmark"
    sequelize = "sequelize"
    sequelize_wordmark = "sequelize_wordmark"
    shopware_original = "shopware_original"
    shopware_original_wordmark = "shopware_original_wordmark"
    sketch_line = "sketch_line"
    sketch_line_wordmark = "sketch_line_wordmark"
    slack = "slack"
    slack_wordmark = "slack_wordmark"
    sourcetree_original = "sourcetree_original"
    sourcetree_original_wordmark = "sourcetree_original_wordmark"
    spring = "spring"
    spring_wordmark = "spring_wordmark"
    spss = "spss"
    sqlalchemy = "sqlalchemy"
    sqlalchemy_original_wordmark = "sqlalchemy_original_wordmark"
    ssh_original = "ssh_original"
    ssh_original_wordmark = "ssh_original_wordmark"
    stylus_original = "stylus_original"
    swift = "swift"
    swift_wordmark = "swift_wordmark"
    symfony_original = "symfony_original"
    symfony_original_wordmark = "symfony_original_wordmark"
    tailwindcss = "tailwindcss"
    tailwindcss_original_wordmark = "tailwindcss_original_wordmark"
    tensorflow_line = "tensorflow_line"
    tensorflow_line_wordmark = "tensorflow_line_wordmark"
    tensorflow_original = "tensorflow_original"
    tensorflow_original_wordmark = "tensorflow_original_wordmark"
    thealgorithms = "thealgorithms"
    thealgorithms_wordmark = "thealgorithms_wordmark"
    tomcat_line = "tomcat_line"
    tomcat_line_wordmark = "tomcat_line_wordmark"
    travis = "travis"
    travis_wordmark = "travis_wordmark"
    trello = "trello"
    trello_wordmark = "trello_wordmark"
    twitter_original = "twitter_original"
    typescript = "typescript"
    typo3 = "typo3"
    typo3_wordmark = "typo3_wordmark"
    ubuntu = "ubuntu"
    ubuntu_wordmark = "ubuntu_wordmark"
    unix_original = "unix_original"
    uwsgi = "uwsgi"
    vagrant = "vagrant"
    vagrant_wordmark = "vagrant_wordmark"
    vim = "vim"
    visualstudio = "visualstudio"
    visualstudio_wordmark = "visualstudio_wordmark"
    vscode = "vscode"
    vscode_wordmark = "vscode_wordmark"
    vuejs = "vuejs"
    vuejs_line = "vuejs_line"
    vuejs_line_wordmark = "vuejs_line_wordmark"
    vuejs_wordmark = "vuejs_wordmark"
    vuestorefront = "vuestorefront"
    weblate = "weblate"
    weblate_wordmark = "weblate_wordmark"
    webpack = "webpack"
    webpack_wordmark = "webpack_wordmark"
    webstorm = "webstorm"
    webstorm_wordmark = "webstorm_wordmark"
    windows8_original = "windows8_original"
    windows8_original_wordmark = "windows8_original_wordmark"
    woocommerce = "woocommerce"
    woocommerce_wordmark = "woocommerce_wordmark"
    wordpress = "wordpress"
    wordpress_wordmark = "wordpress_wordmark"
    xd = "xd"
    xd_line = "xd_line"
    yarn = "yarn"
    yarn_wordmark = "yarn_wordmark"
    yii = "yii"
    yii_wordmark = "yii_wordmark"
    yunohost = "yunohost"
    zend = "zend"
    zend_wordmark = "zend_wordmark"
    zig_original = "zig_original"
    zig_wordmark = "zig_wordmark"