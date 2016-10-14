import { connect } from 'react-redux';
import PredictionGraph from '../components/predictionGraphComponent';

const mapStateToProps = function (state) {
  return {
    data: state.predictionGraph.data,
    isFailed: state.predictionGraph.isFailed,
    isFetching: state.predictionGraph.isFetching
  }
};

const PredictionGraphContainer = connect(
  mapStateToProps
)(PredictionGraph);

export default PredictionGraphContainer;