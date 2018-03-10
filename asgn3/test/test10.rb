class Tables
  def initialize(v)
    @val = v
  end
  def set(v)
    @val = v
  end
  def get
    return @val
  end
  def increment
    @val += 1
  end
  def to_s
    return "Tables(val=" + @val.to_s + ")"
  end
end
a = Tables.new(621)
a.increment
print a, "\n"