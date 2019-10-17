require 'simplecov'
require 'coveralls'

SimpleCov.formatter = Coveralls::SimpleCov::Formatter
SimpleCov.start do
   add_filter "/env/"
   add_filter "/virtualenv/"
   add_filter %r{^/home/}
end