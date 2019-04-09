get.accuracy = function(cm) {
  correct.predictions = sum(diag(cm))
  total.predictions = sum(cm)
  accuracy = (correct.predictions / total.predictions) * 100
  return (accuracy)
}
