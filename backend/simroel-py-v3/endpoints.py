from fastapi import APIRouter, HTTPException
import os
from pydantic import BaseModel
from files.file_manager import FileManager
from files.parameters import Params
parameters_path = os.path.join(os.getcwd(), "simroel-py-v3", "parameters.json")
router = APIRouter()
file_manager = FileManager()


class SlotSizeModel(BaseModel):
    slot_size: float

class CorePitchModel(BaseModel):
    core_pitch: float

class NodeLossModel(BaseModel):
    node_loss: float  # Assuming node_loss should be a float

class FiberLossCoefficientModel(BaseModel):
    fiber_loss_coefficient: float  # Assuming fiber_loss_coefficient should be a float

class NoiseFigureModel(BaseModel):
    noise_figure: float  # Assuming noise_figure should be a float

class ConnectionModel(BaseModel):
    connections: int

class SimulationsModel(BaseModel):
    simulations: int

class ParamsModel(BaseModel):
    params: dict

class CoresModel(BaseModel):
    cores: list

class AllocationTypeModel(BaseModel):
    allocation_type: str

class FiberLossModel(BaseModel):
    fiber_loss_coefficient: float

class TrafficLambdaModel(BaseModel):
    traffic_lambda: float

class RouteAlgorithmModel(BaseModel):
    route_algorithm: str

class PccHoldingTimeModel(BaseModel):
    pcc_holding_time: float

class GuardBandModel(BaseModel):
    guard_band: float

class ConnectionHoldingTimeModel(BaseModel):
    conn_holding_time: float

class ModulationModel(BaseModel):
    modulation: str

class WavelengthModel(BaseModel):
    wavelength: float

class SpanLengthModel(BaseModel):
    span_length: float

class ConfidenceIntervalModel(BaseModel):
    confidence_interval: float

class ThreadNumberModel(BaseModel):
    thread_number: int

class PccTimeThresholdModel(BaseModel):
    pcc_time_threshold: float

class BendingRadiusModel(BaseModel):
    bending_radius: float

class CouplingCoeffModel(BaseModel):
    coupling_coeff: float

class BandRefModel(BaseModel):
    band_ref: float

@router.post("/set_slot_size")
def set_slot_size(slot_size_data: SlotSizeModel):
    try:
        success = file_manager.set_slot_size(slot_size_data.slot_size)
        if success:
            return {"message": "Slot size updated successfully", "new_value": slot_size_data.slot_size}
        else:
            raise HTTPException(status_code=500, detail="Failed to update slot size")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_slot_size")
def get_slot_size():
    try:
        params = file_manager.get_params()
        return {"slot_size": params["slot_size"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class BandwidthModel(BaseModel):
    bandwidth: int
# POST endpoint to receive the bandwi0dth value
@router.post("/set_bandwidth")
def set_bandwidth(bandwidth: BandwidthModel):
    try:
        sucess = file_manager.set_bandwidth(bandwidth.bandwidth)
        if sucess:
            return {"message": "set bandwidth updated successfully", "new_value": bandwidth.bandwidth}
        else:
            raise HTTPException(status_code=500, detail="Failed to update bandwidth")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    #return {"message": "Bandwidth set successfully"}

@router.get("/get_bandwidth")
def get_bandwidth():
    try:
        params = file_manager.get_params()
        return {"bandwidth": params["bandwidth"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    #return {"bandwidth": params.get_bandwidth()}

@router.post("/set_node_loss")
def set_node_loss(node_loss_data: NodeLossModel):
    try:
        success = file_manager.set_node_loss(node_loss_data.node_loss)
        if success:
            return {"message": "Node loss updated successfully", "new_value": node_loss_data.node_loss}
        else:
            raise HTTPException(status_code=500, detail="Failed to update node loss")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_fiber_loss_coefficient")
def set_fiber_loss_coefficient(fiber_loss_data: FiberLossCoefficientModel):
    try:
        success = file_manager.set_fiber_loss_coefficient(fiber_loss_data.fiber_loss_coefficient)
        if success:
            return {"message": "Fiber loss coefficient updated successfully", "new_value": fiber_loss_data.fiber_loss_coefficient}
        else:
            raise HTTPException(status_code=500, detail="Failed to update fiber loss coefficient")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_noise_figure")
def set_noise_figure(noise_figure_data: NoiseFigureModel):
    try:
        success = file_manager.set_noise_figure(noise_figure_data.noise_figure)
        if success:
            return {"message": "Noise figure updated successfully", "new_value": noise_figure_data.noise_figure}
        else:
            raise HTTPException(status_code=500, detail="Failed to update noise figure")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_node_loss")
def get_node_loss():
    try:
        params = file_manager.get_params()
        return {"node_loss": params["node_loss"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_fiber_loss_coefficient")
def get_fiber_loss_coefficient():
    try:
        params = file_manager.get_params()
        return {"fiber_loss_coefficient": params["fiber_loss_coefficient"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_noise_figure")
def get_noise_figure():
    try:
        params = file_manager.get_params()
        return {"noise_figure": params["noise_figure"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/set_core_pitch")
def set_core_pitch(core_pitch_data: CorePitchModel):
    try:
        success = file_manager.set_core_pitch(core_pitch_data.core_pitch)
        if success:
            return {"message": "Slot size updated successfully", "new_value": core_pitch_data.core_pitch}
        else:
            raise HTTPException(status_code=500, detail="Failed to update slot size")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_core_pitch")
def get_core_pitch():
    try:
        params = file_manager.get_params()
        return {"core_pitch": params["core_pitch"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    #return {"core_pitch": params.get_core_pitch()}
@router.post("/set_traffic_lambda")
def set_traffic_lambda(traffic_lambda: TrafficLambdaModel):
    try:
        success = file_manager.set_traffic_lambda(traffic_lambda.traffic_lambda)
        if success:
            return {"message": "Traffic lambda updated successfully", "new_value": traffic_lambda.traffic_lambda}
        else:
            raise HTTPException(status_code=500, detail="Failed to update traffic lambda")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_route_algorithm")
def set_route_algorithm(route_algorithm: RouteAlgorithmModel):
    try:
        success = file_manager.set_route_algorithm(route_algorithm.route_algorithm)
        if success:
            return {"message": "Route algorithm updated successfully", "new_value": route_algorithm.route_algorithm}
        else:
            raise HTTPException(status_code=500, detail="Failed to update route algorithm")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_pcc_holding_time")
def set_pcc_holding_time(pcc_holding_time: PccHoldingTimeModel):
    try:
        success = file_manager.set_pcc_holding_time(pcc_holding_time.pcc_holding_time)
        if success:
            return {"message": "PCC holding time updated successfully", "new_value": pcc_holding_time.pcc_holding_time}
        else:
            raise HTTPException(status_code=500, detail="Failed to update PCC holding time")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_guard_band")
def set_guard_band(guard_band: GuardBandModel):
    try:
        success = file_manager.set_guard_band(guard_band.guard_band)
        if success:
            return {"message": "Guard band updated successfully", "new_value": guard_band.guard_band}
        else:
            raise HTTPException(status_code=500, detail="Failed to update guard band")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_conn_holding_time")
def set_conn_holding_time(conn_holding_time: ConnectionHoldingTimeModel):
    try:
        success = file_manager.set_conn_holding_time(conn_holding_time.conn_holding_time)
        if success:
            return {"message": "Connection holding time updated successfully", "new_value": conn_holding_time.conn_holding_time}
        else:
            raise HTTPException(status_code=500, detail="Failed to update connection holding time")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_modulation")
def set_modulation(modulation: ModulationModel):
    try:
        success = file_manager.set_modulation(modulation.modulation)
        if success:
            return {"message": "Modulation updated successfully", "new_value": modulation.modulation}
        else:
            raise HTTPException(status_code=500, detail="Failed to update modulation")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_wavelength")
def set_wavelength(wavelength: WavelengthModel):
    try:
        success = file_manager.set_wavelength(wavelength.wavelength)
        if success:
            return {"message": "Wavelength updated successfully", "new_value": wavelength.wavelength}
        else:
            raise HTTPException(status_code=500, detail="Failed to update wavelength")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_span_length")
def set_span_length(span_length: SpanLengthModel):
    try:
        success = file_manager.set_span_length(span_length.span_length)
        if success:
            return {"message": "Span length updated successfully", "new_value": span_length.span_length}
        else:
            raise HTTPException(status_code=500, detail="Failed to update span length")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_confidence_interval")
def set_confidence_interval(confidence_interval: ConfidenceIntervalModel):
    try:
        success = file_manager.set_confidence_interval(confidence_interval.confidence_interval)
        if success:
            return {"message": "Confidence interval updated successfully", "new_value": confidence_interval.confidence_interval}
        else:
            raise HTTPException(status_code=500, detail="Failed to update confidence interval")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_thread_number")
def set_thread_number(thread_number: ThreadNumberModel):
    try:
        success = file_manager.set_thread_number(thread_number.thread_number)
        if success:
            return {"message": "Thread number updated successfully", "new_value": thread_number.thread_number}
        else:
            raise HTTPException(status_code=500, detail="Failed to update thread number")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_pcc_time_threshold")
def set_pcc_time_threshold(pcc_time_threshold: PccTimeThresholdModel):
    try:
        success = file_manager.set_pcc_time_threshold(pcc_time_threshold.pcc_time_threshold)
        if success:
            return {"message": "PCC time threshold updated successfully", "new_value": pcc_time_threshold.pcc_time_threshold}
        else:
            raise HTTPException(status_code=500, detail="Failed to update PCC time threshold")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_bending_radius")
def set_bending_radius(bending_radius: BendingRadiusModel):
    try:
        success = file_manager.set_bending_radius(bending_radius.bending_radius)
        if success:
            return {"message": "Bending radius updated successfully", "new_value": bending_radius.bending_radius}
        else:
            raise HTTPException(status_code=500, detail="Failed to update bending radius")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_coupling_coeff")
def set_coupling_coeff(coupling_coeff: CouplingCoeffModel):
    try:
        success = file_manager.set_coupling_coeff(coupling_coeff.coupling_coeff)
        if success:
            return {"message": "Coupling coefficient updated successfully", "new_value": coupling_coeff.coupling_coeff}
        else:
            raise HTTPException(status_code=500, detail="Failed to update coupling coefficient")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/set_band_ref")
def set_band_ref(band_ref: BandRefModel):
    try:
        success = file_manager.set_band_ref(band_ref.band_ref)
        if success:
            return {"message": "Band ref updated successfully", "new_value": band_ref.band_ref}
        else:
            raise HTTPException(status_code=500, detail="Failed to update band ref")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.get("/get_n_connections")
def get_n_connections():
    try:
        connections = file_manager.get_n_connections()#TODO NO file_manager NÃO TEM ESSE
        return {"connections": connections}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_n_simulations")
def get_n_simulations():
    try:
        simulations = file_manager.get_n_simulations()#TODO NO file_manager NÃO TEM ESSE
        return {"simulations": simulations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/load_params")
def load_params():
    try:
        params = file_manager.load_params()#TODO NO file_manager NÃO TEM ESSE
        return {"params": params}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# @router.get("/get_slot_size")
# def get_slot_size():
#     try:
#         params = file_manager.get_params()
#         return {"slot_size": params["slot_size"]}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#
@router.get("/get_n_cores")
def get_n_cores():
    try:
        params = file_manager.get_params()
        return {"n_cores": params["n_cores"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_cores")
def get_cores():
    try:
        cores = file_manager.get_cores() #TODO NO file_manager NÃO TEM ESSE
        return {"cores": cores}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_allocation_type")
def get_allocation_type():
    try:
        params = file_manager.get_params()
        return {"allocation_type": params["allocation_type"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_allocation_fn")
def get_allocation_fn():
    try:
        params = file_manager.get_params()
        return {"allocation_fn": params["allocation_fn"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# @router.get("/get_node_loss")
# def get_node_loss():
#     try:
#         params = file_manager.get_params()
#         return {"node_loss": params["node_loss"]}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
# #
# @router.get("/get_fiber_loss_coefficient")
# def get_fiber_loss_coefficient():
#     try:
#         params = file_manager.get_params()
#         return {"fiber_loss_coefficient": params["fiber_loss_coefficient"]}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
# #
# @router.get("/get_noise_figure")
# def get_noise_figure():
#     try:
#         params = file_manager.get_params()
#         return {"noise_figure": params["noise_figure"]}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#
@router.get("/get_traffic_lambda")
def get_traffic_lambda():
    try:
        params = file_manager.get_params()
        return {"traffic_lambda": params["traffic_lambda"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_traffic_refresh")
def get_traffic_refresh():
    try:
        params = file_manager.get_params()
        return {"traffic_refresh": params["traffic_refresh"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_traffic_file")
def get_traffic_file():
    try:
        params = file_manager.get_params()
        return {"traffic_file": params["traffic_file"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_traffic_conn_types")
def get_traffic_conn_types():
    try:
        params = file_manager.get_params()
        return {"traffic_conn_types": params["traffic_conn_types"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_route_algorithm")
def get_route_algorithm():
    try:
        params = file_manager.get_params()
        return {"route_algorithm": params["route_algorithm"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_k_routes")
def get_k_routes():
    try:
        params = file_manager.get_params()
        return {"k_routes": params["k_routes"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_route_selection")
def get_route_selection():
    try:
        params = file_manager.get_params()
        return {"route_selection": params["route_selection"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_pcc_holding_time")
def get_pcc_holding_time():
    try:
        params = file_manager.get_params()
        return {"pcc_holding_time": params["pcc_holding_time"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_guard_band")
def get_guard_band():
    try:
        params = file_manager.get_params()
        return {"guard_band": params["guard_band"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_conn_holding_time")
def get_conn_holding_time():
    try:
        params = file_manager.get_params()
        return {"conn_holding_time": params["conn_holding_time"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_tracer")
def get_tracer():
    try:
        params = file_manager.get_params()
        return {"tracer": params["tracer"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_osnr")
def get_osnr():
    try:
        params = file_manager.get_params()
        return {"osnr": params["osnr"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_modulation")
def get_modulation():
    try:
        params = file_manager.get_params()
        return {"modulation": params["modulation"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_lambda")
def get_lambda():
    try:
        params = file_manager.get_params()
        return {"lambda": params["lambda"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_fn")
def get_fn():
    try:
        params = file_manager.get_params()
        return {"fn": params["fn"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_p")
def get_p():
    try:
        params = file_manager.get_params()
        return {"p": params["p"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_span_length")
def get_span_length():
    try:
        params = file_manager.get_params()
        return {"span_length": params["span_length"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_band_ref")
def get_band_ref():
    try:
        params = file_manager.get_params()
        return {"band_ref": params["band_ref"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_limit_single_carrier")
def get_limit_single_carrier():
    try:
        params = file_manager.get_params()
        return {"limit_single_carrier": params["limit_single_carrier"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_wavelength")
def get_wavelength():
    try:
        params = file_manager.get_params()
        return {"wavelength": params["wavelength"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_bending_radius")
def get_bending_radius():
    try:
        params = file_manager.get_params()
        return {"bending_radius": params["bending_radius"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_coupling_coeff")
def get_coupling_coeff():
    try:
        params = file_manager.get_params()
        return {"coupling_coeff": params["coupling_coeff"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_port_isolation")
def get_port_isolation():
    try:
        params = file_manager.get_params()
        return {"port_isolation": params["port_isolation"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_crosstalk_reason")
def get_crosstalk_reason():
    try:
        params = file_manager.get_params()
        return {"crosstalk_reason": params["crosstalk_reason"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_calculate_crosstalk")
def get_calculate_crosstalk():
    try:
        params = file_manager.get_params()
        return {"calculate_crosstalk": params["calculate_crosstalk"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_confidence_interval")
def get_confidence_interval():
    try:
        params = file_manager.get_params()
        return {"confidence_interval": params["confidence_interval"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_thread_number")
def get_thread_number():
    try:
        params = file_manager.get_params()
        return {"thread_number": params["thread_number"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_pcc_time_threshold")
def get_pcc_time_threshold():
    try:
        params = file_manager.get_params()
        return {"pcc_time_threshold": params["pcc_time_threshold"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
