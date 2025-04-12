import * as React from "react";
import './parameters.css';
import { useFormContext } from 'react-hook-form';
import { Card } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { FormControl, FormField, FormItem } from "@/components/ui/form";
import { useEffect } from "react";
import {
  fetchSlotSize,
  fetchCorePitch,
  fetchNodeLoss,
  fetchFiberLossCoefficient,
  fetchNoiseFigure,
  fetchTrafficLambda,
  fetchRouteAlgorithm,
  fetchPCCHoldingTime,
  fetchGuardBand,
  fetchConnHoldingTime,
  fetchModulation,
  fetchWavelength,
  fetchSpanLength,
  fetchConfidenceInterval,
  fetchThreadNumber,
  fetchPCCTimeThreshold,
  postSlotSize,
  postCorePitch,
  postNodeLoss,
  postFiberLossCoefficient,
  postNoiseFigure,
  postTrafficLambda,
  postRouteAlgorithm,
  postPCCHoldingTime,
  postGuardBand,
  postConnHoldingTime,
  postModulation,
  postWavelength,
  postSpanLength,
  postConfidenceInterval,
  postThreadNumber,
  postPCCTimeThreshold,
} from './apiservices';

export default function Physical() {
  const { register, control } = useFormContext();

  useEffect(() => {
    fetchSlotSize()
      .then(data => {
        if (data.slot_size) {
          control._formValues.Slot_Size = data.slot_size;
        }
      })
      .catch(error => console.error("Error fetching slot size:", error));

    fetchCorePitch()
      .then(data => {
        if (data.core_pitch) {
          control._formValues.Core_Pitch = data.core_pitch;
        }
      })
      .catch(error => console.error("Error fetching core pitch:", error));

    // Repita para outras chamadas à API...
  }, [control]);

  return (
    <main className="pt-6 pl-4 pr-4 pb-8">
            <Card className="sm:col-span-2" x-chunk="dashboard-05-chunk-0">
                <div className="grid w-full items-start gap-6" >
                    <fieldset className="grid gap-6 rounded-lg border p-4">
                        <div className="grid grid-cols-2 gap-4">
                            <div className="grid grid-cols-2 gap-4">
                                <div className="grid gap-3">
                                    <FormField
                                        control={control}
                                        name="Total_Bandwidth"
                                        render={({field}) => (
                                            <FormItem>
                                                <Label htmlFor="Total_Bandwidth">Total Bandwidth</Label>
                                                <Select
                                                    onValueChange={(value) => {
                                                        // Map the selected value to the desired output
                                                        const bandwidthValue = value === "4" ? 4000 : 9000;

                                                        // Update the field and make the POST request with the mapped value
                                                        field.onChange(bandwidthValue);
                                                        fetch("http://localhost:8000/set_bandwidth", {
                                                            method: "POST",
                                                            headers: {
                                                                "Content-Type": "application/json",
                                                            },
                                                            body: JSON.stringify({bandwidth: bandwidthValue}),
                                                        })
                                                            .then(response => response.json())
                                                            .then(data => console.log("Success:", data))
                                                            .catch(error => console.error("Error:", error));
                                                    }}
                                                    defaultValue="Total_Bandwidth"
                                                >
                                                    <FormControl>
                                                        <SelectTrigger className="input">
                                                            <SelectValue placeholder="Select an option"/>
                                                        </SelectTrigger>
                                                    </FormControl>
                                                    <SelectContent>
                                                        <SelectItem value="4">C Band(4 THz)</SelectItem>
                                                        <SelectItem value="9">S Band(9 THz)</SelectItem>
                                                    </SelectContent>
                                                </Select>
                                            </FormItem>
                                        )}
                                    />
                                </div>
                            </div>
                            <div className="grid grid-cols-2 gap-4">
                                <div className="grid gap-3">
                                    <Label htmlFor="Slot size">Slot size (GHz)</Label>
                                    <Input
                                        className='input'
                                        {...register("Slot_Size")}
                                        type="number"
                                        placeholder="12.5"
                                        min="12.5"
                                        onChange={(e) => {
                                            const value = parseFloat(e.target.value);
                                            console.log("Slot size:", value);  // Para garantir que o valor está correto
                                            fetch("http://localhost:8000/set_slot_size", {
                                                method: "POST",
                                                headers: {
                                                    "Content-Type": "application/json",
                                                },
                                                body: JSON.stringify({slot_size: value}),
                                            })
                                                .then(response => response.json())
                                                .then(data => console.log("Success:", data))
                                                .catch(error => console.error("Error:", error));
                                        }}
                                    />
                                </div>
                            </div>
                            <div className="grid grid-cols-2 gap-4">
                                <div className="grid gap-3">
                                    <Label htmlFor="Node Loss">Node Loss(dB)</Label>
                                    <Input
                                        className="input"
                                        {...register("Node_Loss")}
                                        type="number"
                                        placeholder="16"
                                        min="16"
                                        onBlur={(e) => {
                                            const nodeLossValue = parseFloat(e.target.value);
                                            fetch("http://localhost:8000/set_node_loss", {
                                                method: "POST",
                                                headers: {
                                                    "Content-Type": "application/json",
                                                },
                                                body: JSON.stringify({node_loss: nodeLossValue}),
                                            })
                                                .then(response => response.json())
                                                .then(data => console.log("Success:", data))
                                                .catch(error => console.error("Error:", error));
                                        }}
                                    />
                                </div>
                            </div>
                            <div className="grid grid-cols-2 gap-4">
                                <div className="grid gap-3">
                                    <Label htmlFor="Fiber Loss Coefficient">Fiber Loss Coefficient(dB/km)</Label>
                                    <Input
                                        className="input"
                                        {...register("Fiber_Loss_Coefficient")}
                                        type="number"
                                        placeholder="1"
                                        min="1"
                                        onBlur={(e) => {
                                            const fiberLossValue = parseFloat(e.target.value);
                                            fetch("http://localhost:8000/set_fiber_loss_coefficient", {
                                                method: "POST",
                                                headers: {
                                                    "Content-Type": "application/json",
                                                },
                                                body: JSON.stringify({fiber_loss_coefficient: fiberLossValue}),
                                            })
                                                .then(response => response.json())
                                                .then(data => console.log("Success:", data))
                                                .catch(error => console.error("Error:", error));
                                        }}
                                    />
                                </div>
                            </div>
                            <div className="grid grid-cols-2 gap-4">
                                <div className="grid gap-3">
                                    <Label htmlFor="Noise Figure">Noise Figure(dB)</Label>
                                    <Input
                                        className="input"
                                        {...register("Noise_Figure")}
                                        type="number"
                                        placeholder="5.5"
                                        min="5.5"
                                        onBlur={(e) => {
                                            const noiseFigureValue = parseFloat(e.target.value);
                                            fetch("http://localhost:8000/set_noise_figure", {
                                                method: "POST",
                                                headers: {
                                                    "Content-Type": "application/json",
                                                },
                                                body: JSON.stringify({noise_figure: noiseFigureValue}),
                                            })
                                                .then(response => response.json())
                                                .then(data => console.log("Success:", data))
                                                .catch(error => console.error("Error:", error));
                                        }}
                                    />
                                </div>
                            </div>

                            <div className="grid grid-cols-2 gap-4">
                                <div className="grid gap-3">
                                    <FormField
                                        control={control}
                                        name="Signal_Power"
                                        render={({field}) => (
                                            <FormItem>
                                                <Label htmlFor="Signal_Power">Signal Power</Label>
                                                <Select onValueChange={field.onChange} defaultValue="Signal_Power">
                                                    <FormControl>
                                                        <SelectTrigger className='input'>
                                                            <SelectValue placeholder="Select a option"/>
                                                        </SelectTrigger>
                                                    </FormControl>
                                                    <SelectContent>
                                                        <SelectItem value="mW">mW</SelectItem>
                                                        <SelectItem value="dB">dB</SelectItem>
                                                    </SelectContent>
                                                </Select>
                                            </FormItem>
                                        )}
                                    />
                                </div>
                            </div>
                            <div className="grid grid-cols-2 gap-4">
                                <div className="grid gap-3">
                                    <Label htmlFor="Reference Band">Reference Band (GHz)</Label>
                                    <Input
                                        className='input'
                                        {...register("Reference_Band")}
                                        type="number"
                                        placeholder="12.5"
                                        min="12.5"
                                        onChange={(e) => {
                                            const value = parseFloat(e.target.value);
                                            console.log("Reference Band:", value);
                                            fetch("http://localhost:8000/set_band_ref", {
                                                method: "POST",
                                                headers: {
                                                    "Content-Type": "application/json",
                                                },
                                                body: JSON.stringify({band_ref: value}),
                                            })
                                                .then(response => response.json())
                                                .then(data => console.log("Success:", data))
                                                .catch(error => console.error("Error:", error));
                                        }}
                                    />
                                </div>
                            </div>

                            <div className="grid grid-cols-2 gap-4">
                                <div className="grid gap-3">
                                    <Label htmlFor="Bending Radius">Bending Radius (m)</Label>
                                    <Input
                                        className='input'
                                        {...register("Bending_Radius")}
                                        type="number"
                                        placeholder="1"
                                        min="1"
                                        onChange={(e) => {
                                            const value = parseFloat(e.target.value);
                                            console.log("Bending Radius:", value);
                                            fetch("http://localhost:8000/set_bending_radius", {
                                                method: "POST",
                                                headers: {
                                                    "Content-Type": "application/json",
                                                },
                                                body: JSON.stringify({bending_radius: value}),
                                            })
                                                .then(response => response.json())
                                                .then(data => console.log("Success:", data))
                                                .catch(error => console.error("Error:", error));
                                        }}
                                    />
                                </div>
                            </div>
                            <div className="grid grid-cols-2 gap-4">
                                <div className="grid gap-3">
                                    <Label htmlFor="Coupling Coefficient">Coupling Coefficient (dB/Km)</Label>
                                    <select
                                        className='input'
                                        {...register("Coupling_Coefficient")}
                                        onChange={(e) => {
                                            const value = parseFloat(e.target.value);
                                            console.log("Coupling Coefficient:", value);
                                            fetch("http://localhost:8000/set_coupling_coeff", {
                                                method: "POST",
                                                headers: {
                                                    "Content-Type": "application/json",
                                                },
                                                body: JSON.stringify({coupling_coeff: value}),
                                            })
                                                .then(response => response.json())
                                                .then(data => console.log("Success:", data))
                                                .catch(error => console.error("Error:", error));
                                        }}
                                    >
                                        <option value="">Select Coupling Coefficient</option>
                                        <option value="0.012">1.2 × 10⁻² m⁻¹</option>
                                        <option value="0.00584">5.84 × 10⁻³ m⁻¹</option>
                                    </select>
                                </div>
                            </div>
                            <div className="grid grid-cols-2 gap-4">
                                <div className="grid gap-3">
                                    <Label htmlFor="Core Pitch">Core Pitch(µm)</Label>
                                    <Input className='input' {...register("Core_Pitch")}
                                           type="number"
                                           placeholder="45"
                                           min="45"
                                           onChange={(e) => {
                                               const value = parseFloat(e.target.value);
                                               console.log("Core Pitch:", value);  // Para garantir que o valor está correto
                                               fetch("http://localhost:8000/set_core_pitch", {
                                                   method: "POST",
                                                   headers: {
                                                       "Content-Type": "application/json",
                                                   },
                                                   body: JSON.stringify({core_pitch: value}),
                                               })
                                                   .then(response => response.json())
                                                   .then(data => console.log("Success:", data))
                                                   .catch(error => console.error("Error:", error));
                                           }}

                                    />
                                </div>
                            </div>
                            <div className="grid grid-cols-2 gap-4">
                                <div className="grid gap-3">
                                    <FormField
                                        control={control}
                                        name="Coupling_factor"
                                        render={({field}) => (
                                            <FormItem>
                                                <Label htmlFor="Coupling_factor">Coupling factor</Label>
                                                <Select onValueChange={field.onChange} defaultValue="Coupling_factor">
                                                    <FormControl>
                                                        <SelectTrigger className='input'>
                                                            <SelectValue placeholder="Select a option"/>
                                                        </SelectTrigger>
                                                    </FormControl>
                                                    <SelectContent>
                                                        <SelectItem value="1.2">1.2 x 10⁻²m⁻¹</SelectItem>
                                                        <SelectItem value="5.84">5.84 x 10⁻³m⁻¹</SelectItem>
                                                    </SelectContent>
                                                </Select>
                                            </FormItem>
                                        )}
                                    />
                                </div>
                            </div>
                        </div>
                    </fieldset>

                </div>
            </Card>
        </main>
  );
}