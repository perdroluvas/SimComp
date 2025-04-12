/*Pagina para parametros de simulacao*/
import * as React from "react";
import "./parameters.css"
import {useFormContext} from 'react-hook-form';
import {Card} from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select"
import {
    FormControl,
    FormField,
    FormItem,
  } from "@/components/ui/form"

export default function Simulation() {
    const {register,control}= useFormContext();
    return (
        <main className="pt-6 pl-4 pr-4 pb-8">
            <Card className="sm:col-span-2" x-chunk="dashboard-05-chunk-0">
            <div className="grid w-full items-start gap-6" >
                    <fieldset className="grid gap-6 rounded-lg border p-4">
                        <div className="grid grid-cols-2 gap-4">
                        <div className="grid grid-cols-2 gap-4">
                            <div className="grid gap-3">
                                <Label htmlFor="N_simulations">Number of simulations</Label>
                                <Input className='input' {...register('N_simulations',{required:true})} type="number" placeholder="1" min="1" />
                                
                            </div>
                            </div>
                        <div className="grid grid-cols-2 gap-4">
                            <div className="grid gap-3">
                                <FormField
                                control={control}
                                name="Calc_OSRN"
                                render={({field})=>(
                                <FormItem>
                                <Label htmlFor="Calc_OSRN">Calculate OSRN (dB)</Label>
                                <Select onValueChange={field.onChange} defaultValue="Calc_OSRN">
                                    <FormControl>
                                    <SelectTrigger className='input'>
                                        <SelectValue placeholder="Select  is on or off" />
                                    </SelectTrigger>
                                    </FormControl>
                                    <SelectContent >
                                        <SelectItem value="on" >On</SelectItem>
                                        <SelectItem value="off">Off</SelectItem>
                                    </SelectContent>
                                </Select>
                                </FormItem>
                                )}
                                />
                            </div>
                            </div>
                            <div className="grid grid-cols-2 gap-4 ">
                            <div className="grid gap-3">
                                <Label htmlFor="Traffic lambda">Traffic lambda</Label>
                                <Input className='input' {...register('Traffic_lambda',{required:true})} type="number" placeholder="1" min="1" />
                                
                            </div>
                        </div>
                            <div className="grid grid-cols-2 gap-4">
                            <div className="grid gap-3">
                            <FormField
                                control={control}
                                name="Calc_Crosstalk"
                                render={({field})=>(
                                <FormItem>
                                <Label htmlFor="Calc_Crosstalk">Calculate Crosstalk intercore(dB)</Label>
                                <Select onValueChange={field.onChange} defaultValue="Calc_Crosstalk">
                                    <FormControl>
                                    <SelectTrigger className='input'>
                                        <SelectValue placeholder="Select a is on or off" />
                                    </SelectTrigger>
                                    </FormControl>
                                    <SelectContent >
                                        <SelectItem value="on" >On</SelectItem>
                                        <SelectItem value="off">Off</SelectItem>
                                    </SelectContent>
                                </Select>
                                </FormItem>
                                )}
                                />
                            </div>
                            </div>
                        </div>
                    </fieldset>
                    <fieldset className="grid gap-6 rounded-lg border p-4">
                        <div className="grid grid-cols-2 gap-4">
                        <div className="grid grid-cols-2 gap-4">
                            <div className="grid gap-3">
                                <Label htmlFor="Min_load">Minimum load</Label>
                                <Input className='input' {...register('Min_load',{required:true})} type="number" placeholder="1" min="1" />
                            </div>
                            </div>
                            <div className="grid grid-cols-2 gap-4">
                            <div className="grid gap-3">
                                <Label htmlFor="Max_load">Maximum load</Label>
                                <Input className='input' {...register('Max_load',{required:true})} type="number" placeholder="1" min="1" />
                            </div>
                            </div>
                            <div className="grid grid-cols-2 gap-4">
                            <div className="grid gap-3">
                                <Label htmlFor="load_range">load range</Label>
                                <Input className='input' {...register('load_range',{required:true})} type="number" placeholder="1" min="1" />
                            </div>
                            </div>
                            </div>
                    </fieldset>
                    </div>
            </Card>
        </main>
    )
}
